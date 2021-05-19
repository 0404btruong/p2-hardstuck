from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request
from people.Kian.bubblesort import numberSort

people_Kian_bp = Blueprint('people_kian', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@people_Kian_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csp2021tri3")

@people_Kian_bp.route('/bubblesort',methods=['GET', 'POST'])

def bubblesort():
    start = [1, 4, 7, 3, 5]
    if request.method=='POST':
        before = [int(n) for n in request.args.get("numList")]
    return render_template("bubblesort.html", start=start, finish=numberSort(start))

