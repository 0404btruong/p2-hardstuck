from flask import Flask, render_template
from flask_login import (UserMixin)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from people import people_bp
from people.Brandon import people_Brandon_bp
from people.David import people_David_bp
from people.Gavin import people_Gavin_bp
from people.Kian import people_Kian_bp
from people.Cody import people_Cody_bp
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

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/itunes')
def itunes():
    return render_template("itunes.html")

@app.route('/soundcloud')
def soundcloud():
    return render_template("soundcloud.html")

@app.route('/spotify')
def spotify():
    return render_template("spotify.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")


