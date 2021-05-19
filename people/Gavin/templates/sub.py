from flask import Flask, render_template, request, redirect

import smtplib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/email', methods = ['POST'])
def email():
    email = request.form['email']
    email_text = 'Subject: {}\n\n{}'.format("United States Data", 'United States Total Cases 24,983,892; Total Deaths 2,080,972; Current Active Cases 25,361,201 ')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('p2hardstuck@gmail.com', 'MrMadman33')
    server.sendmail('wildcatsp4@gmail.com', email, email_text)
    server.close()
    print ("email sent to:", email)
    return render_template("home.html")