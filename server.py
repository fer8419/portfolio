from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page>')
def get_page(page='/index.html'):
    return render_template(page)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/contact.html')
    except:
        return 'did not save to database'


def write_to_file(data):
    with open('./db/database.txt', mode='a') as db:
        # db.write(','.join(data.keys()))
        db.write('\n')
        db.write(','.join(data.values()))


def write_to_csv(data):
    with open('./db/database.csv', mode='a', newline='') as db:
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
