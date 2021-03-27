from flask import Flask, Blueprint, render_template
from people import people_bp
from people.prep import people_prep_bp
from people.David import people_David_bp
from people.Brandon import people_Brandon_bp
from people.Kian import people_Kian_bp
from people.Gavin import people_Gavin_bp


app = Flask(__name__)
app.register_blueprint(people_bp, url_prefix='/people/repos')
app.register_blueprint(people_prep_bp, url_prefix='/people/prep')
app.register_blueprint(people_David_bp, url_prefix='/people/David')
app.register_blueprint(people_Brandon_bp, url_prefix='/people/Brandon')
app.register_blueprint(people_Kian_bp, url_prefix='/people/Kian')
app.register_blueprint(people_Gavin_bp, url_prefix='/people/Gavin')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/itunes')
def index():
    return render_template("itunes.html")

@app.route('/soundcloud')
def index():
    return render_template("soundcloud.html")

@app.route('spotify')
def index():
    return render_template("spotify.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")
