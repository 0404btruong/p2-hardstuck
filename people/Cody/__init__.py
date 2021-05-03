from flask import Blueprint, render_template

people_Cody_bp = Blueprint('people_Cody', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@people_Cody_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")
