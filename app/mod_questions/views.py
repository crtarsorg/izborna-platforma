# coding=utf-8
import pprint

from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
from bson import json_util

mod_questions = Blueprint('questions', __name__, url_prefix="/questions",static_folder="static", template_folder='templates', )
#get data for all territories selected by year
@mod_questions.route('/', methods=['GET'])
def questions_page():
    return render_template('questions/questions.html',year=0)



