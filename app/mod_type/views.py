# coding=utf-8
import pprint

from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
from bson import json_util
import cyrtranslit
from slugify import slugify
from tqdm import tqdm

mod_type = Blueprint('type', __name__, url_prefix="/type",static_folder="static", template_folder='templates', )

#get data for all territories selected by year
@mod_type.route('/<int:datasource>/<string:typeizbori>/<int:year>/<int:instanca>/krug/<string:krug>', methods=['GET'])
def electionType(datasource, typeizbori,year, instanca, krug):
    data= []
    if typeizbori!="predsjednicki":
        if year==2000:
            url= "http://datacentar.io/api/izbori/1/"+str(typeizbori)+"/godina/"+str(year)+"/instanca/3/krug/none"
        elif year in [2007,2016]:
            url = "http://datacentar.io/api/izbori/1/" + str(typeizbori) + "/godina/" + str(year) + "/instanca/3/krug/none"
        else:
            url = "http://datacentar.io/api/izbori/2/" + str(typeizbori) + "/godina/" + str(year) + "/instanca/3/krug/none"
    else:
        if year==2004:
            url = "http://datacentar.io/api/izbori/2/" + str(typeizbori) + "/godina/" + str(year) + "/instanca/4/krug/"+str(krug)
        else:
            url = "http://datacentar.io/api/izbori/2/" + str(typeizbori) + "/godina/" + str(year) + "/instanca/3/krug/" + str(krug)

    response= urllib.urlopen(url)
    for line in json.loads(response.read()):
        data.append(line)


    #get all territories by selected year
    territories=[]
    if typeizbori != "predsjednicki":
        if year == 2000:
            urlterritories="http://datacentar.io/api/izbori/1/"+str(typeizbori)+"/godina/"+str(year)+"/teritorija/instanca/3"
        elif year in [2007,2016]:
            urlterritories = "http://datacentar.io/api/izbori/winners/1/parlamentarni/godina/" + str(year) + "/instanca/3"
        else:
            urlterritories = "http://datacentar.io/api/izbori/winners/2/parlamentarni/godina/" + str(year) + "/instanca/3"
    else:
        urlterritories = "http://datacentar.io/api/izbori/2/predsjednicki/godina/" + str(year) + "/krug/"+str(krug)+"/teritorija"

    responseterritories = urllib.urlopen(urlterritories)
    for territory in json.loads(responseterritories.read()):
        territories.append(territory)


    #total voters turnout

    urlturnout = "http://datacentar.io/api/izbori/datasource/2/" + str(typeizbori) + "/godina/" + str(year)
    response_turnout = urllib.urlopen(urlturnout)
    results_voters=json.loads(response_turnout.read())

    #get all political parties
    url_political_parties = "http://datacentar.io/api/izbori/parties"
    response_political_parties = urllib.urlopen(url_political_parties)
    list_political_parties = json_util.loads(response_political_parties.read())


    #get winners for each territory
    winner_territory = []
    if year==2000:
        url_winner_territory = "http://datacentar.io/api/izbori/1/"+str(typeizbori)+"/godina/"+str(year)+"/teritorija/instanca/3"
    elif year in [2007,2016]:
        url_winner_territory = "http://datacentar.io/api/izbori/winners/1/" + str(typeizbori) + "/godina/" + str(year) + "/instanca/3"
    else:
        url_winner_territory = "http://datacentar.io/api/izbori/winners/2/" + str(typeizbori) + "/godina/" + str(year)+"/instanca/3"
    response_winner = urllib.urlopen(url_winner_territory)

    for winner in json_util.loads(response_winner.read()):
        winner_territory.append(winner)
    print winner_territory
    return render_template('type/type.html',typeizbori=typeizbori,year=year,data=data,territories=territories,results_voters=results_voters,list_political_parties=list_political_parties,winner_territory=winner_territory,slugify_cr=slugify_cr)

def slugify_cr(s):
     return slugify(cyrtranslit.to_latin(s, 'sr'), to_lower=True)



