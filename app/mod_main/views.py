
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
    #year 2014 parlamentary
    data2014 = []
    url2014 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2014/instanca/4"
    response2014 = urllib.urlopen(url2014)
    for line2014 in json.loads(response2014.read()):
        data2014.append(line2014)
    #end of year 2014 parlamentary

    data2016 = []
    url2016 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2016/instanca/4"
    response2016 = urllib.urlopen(url2016)
    for line2016 in json.loads(response2016.read()):
        data2016.append(line2016)
    #end of year 2016 presidential

    data2008pres=[]
    url2008pres = "http://datacentar.io/api/izbori/1/predsjednicki/godina/2008/instanca/1"
    response2008pres = urllib.urlopen(url2008pres)
    for line2008pres in json.loads(response2008pres.read()):
        data2008pres.append(line2008pres)

    data2012pres = []
    url2012pres = "http://datacentar.io/api/izbori/1/predsjednicki/godina/2012/instanca/1"
    response2012pres = urllib.urlopen(url2012pres)
    for line2012pres in json.loads(response2012pres.read()):
        data2012pres.append(line2012pres)

    url_political_parties = "http://datacentar.io/api/izbori/parties"
    response_political_parties = urllib.urlopen(url_political_parties)
    list_political_parties = json_util.loads(response_political_parties.read())

    return render_template('site/home.html',data2014=data2014, data2016=data2016,data2008pres=data2008pres,data2012pres=data2012pres,list_political_parties=list_political_parties)
