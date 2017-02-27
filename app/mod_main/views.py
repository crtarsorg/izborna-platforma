
from flask import Blueprint
from flask import render_template
import json,urllib
import heapq


mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():

    return render_template('site/home.html',year=0)
