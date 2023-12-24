from flask import Flask, render_template,  url_for, request, redirect
import csv
import os

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

# @app.route("/index.html")
# def home():
#     return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# custom database using txt file
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n {email}, {subject}, {message}')

# @app.route("/submit_form", methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST' :
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again!'


# Custom database using csv 
def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a')  as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,  )
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' :
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again!'



