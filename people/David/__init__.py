from flask import Blueprint, render_template

people_David_bp = Blueprint('people_David', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@people_David_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")

