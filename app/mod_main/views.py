
from flask import Blueprint
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
import heapq

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    #year 2014
    data2014 = []
    url2014 = "http://0.0.0.0:5006/api/izbori/2/parlamentarni/godina/2014/instanca/4"
    response2016 = urllib.urlopen(url2014)
    for line2016 in json.loads(response2016.read()):
        data2014.append(line2016)
    #end of year 2014

    data2016 = []
    url2016 = "http://0.0.0.0:5006/api/izbori/2/parlamentarni/godina/2016/instanca/4"
    response2016 = urllib.urlopen(url2016)
    for line2016 in json.loads(response2016.read()):
        data2016.append(line2016)


    return render_template('site/home.html',data2014=data2014, data2016=data2016)
