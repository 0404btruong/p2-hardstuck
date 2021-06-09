import smtplib
import ssl

import requests
from flask import Flask, render_template, request
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from people import people_bp
from people.Brandon import people_Brandon_bp
from people.Cody import people_Cody_bp
from people.David import people_David_bp
from people.Gavin import people_Gavin_bp
from people.Kian import people_Kian_bp
from people.prep import people_prep_bp

dbURI ='sqlite:///authuser.sqlite3'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = dbURI
app.config['SECRET_KEY'] = 'my_secret_key'
db = SQLAlchemy(app)
app.register_blueprint(people_bp, url_prefix='/people/repos')
app.register_blueprint(people_prep_bp, url_prefix='/people/prep')
app.register_blueprint(people_David_bp, url_prefix='/people/David')
app.register_blueprint(people_Brandon_bp, url_prefix='/people/Brandon')
app.register_blueprint(people_Kian_bp, url_prefix='/people/Kian')
app.register_blueprint(people_Gavin_bp, url_prefix='/people/Gavin')
app.register_blueprint(people_Cody_bp, url_prefix='/people/Cody')

#starting logins
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return AuthUser.query.get(user_id)


class AuthUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(500))
    email = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {"name": self.name,
                "email": self.email}

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

@app.route('/x')
def inde():
    headers1 = {'Authorization': 'db1bcf13c1c3'}
    headers2 = {'client_id': '239', 'redirect_uri': 'https://soundcloud.com', 'response_type': 'code', 'scope': 'default'}
    headers3 = {'key1': 'db&data'}
    headers4 = {'Authorization': 'ea02849ff83b'}
    spotify = requests.get("https://api.spotify.com/", headers=headers1)
    soundcloud = requests.get("https://api.soundcloud.com/", headers=headers2)
    itunes = requests.get("https://api.itunes.com/", headers=headers3)
    youtube = requests.get("https://www.googleapis.com/youtube/v3/", headers=headers4)

    top_music = [spotify["top"]["name"][0:3], soundcloud["top"]["all"]["title"][0:3], itunes["top"]["all"][0:3], youtube["music"]["leaderboard"]["all"]["name"][0:3]]

    return render_template("index.html", top_music=top_music, spotify=spotify, soundcloud=soundcloud, itunes=itunes, youtube=youtube)

@app.route('/itunes')
def itunes():
    return render_template("itunes.html")

@app.route('/soundcloud')
def soundcloud():
    return render_template("soundcloud.html")

@app.route('/spotify')
def spotify():
    return render_template("spotify.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/email', methods = ['GET','POST'])
def email():
    if request.method == 'POST':
        email = request.form['email']
        email_text = 'Subject: {}\n\n{}'.format("MUSIC APP", 'THANK YOU FOR SUBSCRIBING TO THE P2HARDSTUCK MUSIC APP')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465,context=ssl.create_default_context())
        server.login('p2hardstuck@gmail.com', 'CompSci1234!')
        server.sendmail('p2hardstuck@gmail.com', email, email_text)
        server.close()
        print ("email sent to:", email)
        return render_template("sub.html")
    else:
        return render_template("email.html")

@app.route('/')
def index():
    top_music = [["Into the Thick of it", "Talking to the Moon", "Peaches"], ["Into the Thick of it", "Peaches", "Besides you"], ["Into the Thick of it", "Talking to the Moon", "Peaches"], ["Into the Thick of it", "Peaches", "Besides you"], ["Talking to the Moon", "Peaches", "Champaign and Sunshine"]]

    return render_template("index.html", top_music=top_music)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5000")


