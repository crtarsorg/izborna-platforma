import pprint
from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
from bson import json_util

mod_type = Blueprint('type', __name__, url_prefix="/type",static_folder="static", template_folder='templates', )

#get data for all territories selected by year
@mod_type.route('/<int:datasource>/<string:typeizbori>/<int:year>/<int:instanca>', methods=['GET'])
def electionType(datasource, typeizbori,year, instanca):
    data= []
    url= "http://datacentar.io/api/izbori/2/"+str(typeizbori)+"/godina/"+str(year)+"/instanca/"+str(instanca)
    response= urllib.urlopen(url)
    for line in json.loads(response.read()):
        data.append(line)
    #get all territories by selected yea
    territories=[]
    urlterritories="http://datacentar.io/api/izbori/2/"+str(typeizbori)+"/godina/"+str(year)+"/teritorija/instanca/3"
    responseterritories = urllib.urlopen(urlterritories)
    for territory in json.loads(responseterritories.read()):
        territories.append(territory)

    #total voters turnout
    total_percentage=0
    urlturnout="http://datacentar.io/api/izbori/parlamentarni/godina/"+str(year)
    response_turnout = urllib.urlopen(urlturnout)
    total_percentage=response_turnout.read();

    #get all political parties
    url_political_parties = "http://datacentar.io/api/izbori/parties"
    response_political_parties = urllib.urlopen(url_political_parties)
    list_political_parties = json_util.loads(response_political_parties.read())


    #get winners for each territory
    winner_territory = []
    url_winner_territory = "http://datacentar.io/api/izbori/api/izbori/winners/2/"+str(typeizbori)+"/godina/"+str(year)+"/instanca/3"
    response_winner = urllib.urlopen(url_winner_territory)
    for winner in json_util.loads(response_winner.read()):
        winner_territory.append(winner)
    return render_template('type/type.html',typeizbori=typeizbori,year=year,data=data,territories=territories,total_percentage=total_percentage,list_political_parties=list_political_parties,winner_territory=winner_territory)


