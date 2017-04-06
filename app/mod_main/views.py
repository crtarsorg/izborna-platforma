
from flask import Blueprint
from flask import render_template,redirect
import json,urllib
import heapq
mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    return redirect("/sr", code=302)

@mod_main.route('/<lang_code>', methods=['GET'])
def root():
    return render_template('site/home.html',year=0)

