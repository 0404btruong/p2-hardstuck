from flask import Blueprint, render_template

people_bp = Blueprint('people_repos', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@people_bp.route('/')
def index():
    return render_template("course/repos.html")

