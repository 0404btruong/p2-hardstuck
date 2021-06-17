import smtplib
import ssl
import json

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
from random import randint
from myglobals import most_loved_50

dbURI = 'sqlite:///authuser.sqlite3'

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

# starting logins
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return AuthUser.query.get(user_id)


class AuthUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
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


@app.route('/')
def index():
    random45 = randint(0, 45)
    music_recommendations = [most_loved_50["loved"][random45 + k]["strTrack"] for k in range(5)]

    return render_template("index.html", music_recommendations=music_recommendations)


@app.route('/songlookup', methods=["GET", "POST"])
def songlookup():
    return render_template("songlookup.html", requested=False)


@app.route('/songlookup/result', methods=["GET", "POST"])
def songlookupresult():
    if request.form:
        print(request.form.get("lookupsong"))
        print(request.form.get("lookupartist"))
        url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"
        querystring = {"s": request.form.get("lookupartist"), "t": request.form.get("lookupsong")}
        headers = {
            'x-rapidapi-key': "76cb9878c6msh4134b7ab3f64772p18a780jsn44ce0d13cb7d",
            'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
        }
        songinfo = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
        print(songinfo)
        print(type(songinfo))
        return render_template("songlookupresult.html", requested=True, songdata=songinfo)
    else:
        return render_template("songlookupresult.html", requested=False)


@app.route('/quiz/artist', methods=["GET", "POST"])
def artistquiz():
    random50 = randint(0, 50)
    song = most_loved_50["loved"][random50]["strTrack"]
    genre = most_loved_50["loved"][random50]["strGenre"]
    artist = most_loved_50["loved"][random50]["strArtist"]
    if request.form:
        if request.form.get("artistguess").lower() == request.form.get("artistcorrect").lower():
            correct = "correct"
        else:
            correct = "incorrect"
    else:
        correct = "neither right or wrong, as you haven't guessed in this session yet, so there was no"
    return render_template("artistquiz.html", most_loved_50=most_loved_50, song=song, genre=genre, artist=artist, correct=correct)


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


@app.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        email = request.form['email']
        email_text = 'Subject: {}\n\n{}'.format("MUSIC APP", 'THANK YOU FOR SUBSCRIBING TO THE P2HARDSTUCK MUSIC APP')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
        server.login('p2hardstuck@gmail.com', 'CompSci1234!')
        server.sendmail('p2hardstuck@gmail.com', email, email_text)
        server.close()
        print("email sent to:", email)
        return render_template("sub.html")
    else:
        return render_template("email.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5000")
