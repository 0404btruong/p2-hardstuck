from flask import Flask, render_template, request, redirect, flash
from flask_login import (UserMixin, LoginManager, login_required, login_user, current_user, logout_user)
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

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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

@login_manager.user_loader
def load_user(user_id):
    return AuthUser.query.get(user_id)

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

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    print(request.form.get("username"))
    if request.form.get("username") != "" and request.form.get("username") is not None:
        this_user = AuthUser.query.filter_by(name=request.form.get("username")).first()
        print ('1')
        if this_user and AuthUser.check_password(this_user, password=request.form.get("password")):
            login_user(this_user)
            print ('2')
            return redirect('/')
    print ('3')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        logout_user()
        return redirect('/')

    if request.form.get("username") != "" and request.form.get("username") is not None:
        if AuthUser.query.filter_by(name=request.form.get("username")).first() is not None:
            flash ("Username already in use")
            print ("Username already in use")
            return render_template('signup.html')

        if AuthUser.query.filter_by(email=request.form.get("email")).first() is not None:
            flash ("Email address already in use")
            print ("Email address already in use")
            return render_template('signup.html')

        new_user = AuthUser(request.form.get("username"), generate_password_hash(request.form.get("password"), method='sha256'), request.form.get("email"))
        db.session.add(new_user)
        db.session.commit()
        flash ("Sign up successful")
        print ("Sign up successful")
        return render_template("login.html")
    return render_template('signup.html')

if __name__ == "__main__":
    # runs the application on the repl development server

    """AuthUser.query.delete()
    user1 = AuthUser("John", generate_password_hash('password1', method='sha256'), "John@gmail.com")
    user2 = AuthUser("Paul", generate_password_hash('password2', method="sha256"), "Paul@gmail.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()"""

    app.run(debug=True, port="5001")


