
from flask import Blueprint
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
import heapq

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    yearsList = ["2008","2012", "2013", "2014", "2015", "2016"]
    return render_template('site/home.html', yearsList=yearsList,urllib=urllib,json=json,heapq=heapq)
