from flask import Blueprint, render_template

people_Kian_bp = Blueprint('people_kian', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@people_Kian_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csp2021tri3")

