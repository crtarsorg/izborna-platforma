
from flask import Blueprint
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
import heapq
from bson import json_util

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():

    return render_template('site/home.html')
