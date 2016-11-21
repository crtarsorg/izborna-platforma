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
    url= "http://datacentar.io/api/izbori/"+str(datasource)+"/"+str(typeizbori)+"/godina/"+str(year)+"/instanca/"+str(instanca)
    response= urllib.urlopen(url)
    for line in json.loads(response.read()):
        data.append(line)
    return render_template('type/type.html',typeizbori=typeizbori,year=year,data=data)

