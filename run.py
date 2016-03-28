import os
from flask import Flask
from flask import render_template
from flask import request
from sendmail import sendmail
app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello :)'


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	if request.method == 'GET':
		return render_template('contact.html')
	elif (request.method == 'POST'):
		name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        sendmail(name,email,subject,message)
        return "Message sent!"


app.run(debug=True,host="0.0.0.0",port=8080)
