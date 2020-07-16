    # must be run from the SandyPyprog/Flask/venv/
    #$env:FLASK_APP = "server.py"
    #$env:FLASK_ENV = "development" # sets the debug mode on
    #flask run # runs the enviorment
    

# never save something as flask.py...it causes a conflict
from flask import Flask, render_template, url_for, request, redirect # need to import flask
import csv # the csv module is not in flask, so we need to import stand alone!!!!


app = Flask(__name__) # flask is a class to instantiate
print(__name__) # remember to underscores

@app.route('/') # this s decorator ...this slash is setting up our server
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>') #
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to data base"
    else:
        return "something went wrong. Try again"




"""
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return "form submitted hoorayyy!



@app.route('/works.html') # 
def works():
    return render_template("works.html")

@app.route('/contact.html') # 
def contact():
    return render_template("contact.html")

#home and index
@app.route('/index.html') # 
def index():
    return render_template("index.html")

"""