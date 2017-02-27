# coding=utf-8
import pprint

from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
from bson import json_util

mod_type = Blueprint('type', __name__, url_prefix="/type",static_folder="static", template_folder='templates')
#get data for all territories selected by year
@mod_type.route('/<int:datasource>/<string:typeizbori>/<int:year>/<int:instanca>/krug/<string:krug>/status/<string:status>', methods=['GET'])
def electionType(datasource, typeizbori,year, instanca, krug, status):

    return render_template('type/type.html',typeizbori=typeizbori,year=year,instanca=instanca, krug=krug, status=status)



