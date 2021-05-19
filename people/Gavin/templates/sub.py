from flask import Flask, render_template, request, redirect

import smtplib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/email', methods = ['GET','POST'])
def email():
    email = request.form['email']
    email_text = 'Subject: {}\n\n{}'.format("P2Hardstucks MUSIC APP", 'THANK YOU FOR SUBSCRIBING TO OUR MUSIC APP')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('P2Hardstucks@gmail.com', 'morty1234')
    server.sendmail('P2Hardstucks@gmail.com', email, email_text)
    server.close()
    print ("email sent to:", email)
    return render_template("home.html")