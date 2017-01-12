
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
    url2014 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2014/instanca/4/krug/None"
    response2014 = urllib.urlopen(url2014)
    for line2014 in json.loads(response2014.read()):
        data2014.append(line2014)
    #end of year 2014 parlamentary

    data2012 = []
    url2012 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2012/instanca/4/krug/None"
    response2012 = urllib.urlopen(url2012)
    for line2012 in json.loads(response2012.read()):
        data2012.append(line2012)
    #end of year 2012 presidential

    data2008pres=[]
    url2008pres = "http://datacentar.io/api/izbori/2/predsjednicki/godina/2008/instanca/1/krug/prvi"
    response2008pres = urllib.urlopen(url2008pres)
    for line2008pres in json.loads(response2008pres.read()):
        data2008pres.append(line2008pres)

    data2012pres = []
    url2012pres = "http://datacentar.io/api/izbori/2/predsjednicki/godina/2012/instanca/1/krug/prvi"
    response2012pres = urllib.urlopen(url2012pres)
    for line2012pres in json.loads(response2012pres.read()):
        data2012pres.append(line2012pres)

    url_political_parties = "http://datacentar.io/api/izbori/parties"
    response_political_parties = urllib.urlopen(url_political_parties)
    list_political_parties = json_util.loads(response_political_parties.read())

    winner_territory_2014 = []
    url_winner_territory_2014 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2014/teritorija/instanca/3"
    response_winner_2014 = urllib.urlopen(url_winner_territory_2014)
    for winner in json_util.loads(response_winner_2014.read()):
        winner_territory_2014.append(winner)

    winner_territory_2012= []
    url_winner_territory_2012 = "http://datacentar.io/api/izbori/2/parlamentarni/godina/2012/teritorija/instanca/3"
    response_winner_2012 = urllib.urlopen(url_winner_territory_2012)
    for winner in json_util.loads(response_winner_2012.read()):
        winner_territory_2012.append(winner)

    pres_winner_territory_2012 = []
    pres_url_winner_territory = "http://datacentar.io/api/izbori/winners/2/predsjednicki/godina/2012/instanca/3/krug/drugi"
    pres_response_winner_2012 = urllib.urlopen(pres_url_winner_territory)
    for winner1 in json_util.loads(pres_response_winner_2012.read()):
        pres_winner_territory_2012.append(winner1)

    return render_template('site/home.html',
                           data2014=data2014,
                           data2012=data2012,
                           data2008pres=data2008pres,
                           data2012pres=data2012pres,
                           list_political_parties=list_political_parties,
                           winner_territory_2014=winner_territory_2014,
                           winner_territory_2012=winner_territory_2012,
                           pres_winner_territory_2012=pres_winner_territory_2012
                           )
