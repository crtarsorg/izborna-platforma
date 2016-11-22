import pprint
from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib

mod_type = Blueprint('type', __name__, url_prefix="/type",static_folder="static", template_folder='templates', )

#get data for all territories selected by year
@mod_type.route('/<int:datasource>/<string:typeizbori>/<int:year>/<int:instanca>', methods=['GET'])
def electionType(datasource, typeizbori,year, instanca):
    data= []
    url= "http://0.0.0.0:5006/api/izbori/"+str(datasource)+"/"+str(typeizbori)+"/godina/"+str(year)+"/instanca/"+str(instanca)
    response= urllib.urlopen(url)
    for line in json.loads(response.read()):
        data.append(line)
    #get all territories by selected yea
    territories=[]
    urlterritories="http://0.0.0.0:5006/api/izbori/"+str(datasource)+"/"+str(typeizbori)+"/godina/"+str(year)+"/teritorija/instanca/3"
    responseterritories = urllib.urlopen(urlterritories)
    for territory in json.loads(responseterritories.read()):
        territories.append(territory)
    return render_template('type/type.html',typeizbori=typeizbori,year=year,data=data,territories=territories)

