from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__, template_folder='template')
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write('\n {0},{1},{2}'.format(email, subject, message))

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer = database2.write('\n{0},{1},{2}'.format(email, subject, message))
          

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        else:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'