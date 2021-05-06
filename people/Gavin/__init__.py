from flask import Blueprint, render_template
from people.Gavin.gavinsminilab import Superhero

from people.Gavin.bubble2 import sort

people_Gavin_bp = Blueprint('people_Gavin', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@people_Gavin_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")


@people_Gavin_bp.route('/minilab')
def minilab():
    return render_template("minilab.html", superherobest=Superhero(1))


@people_Gavin_bp.route('/bubble2')
def bubble2():
    before = [5, 3, 8, 6, 7, 2, ]
    return render_template("bubble2.html", before=before, after=sort(before))
