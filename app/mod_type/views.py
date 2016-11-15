import pprint
from flask import Blueprint,request
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib

mod_type = Blueprint('type', __name__, url_prefix="/type",static_folder="static", template_folder='templates', )

#get data for all territories selected by year
@mod_type.route('/parlamentarni/<int:year>', methods=['GET'])
def parlamentarni(year):
    if request.method == 'GET':
        data = []
        url = "http://datacentar.io/api/izbori/parlamentarni/godina/"+str(year)+"/teritorija"
        response = urllib.urlopen(url)
        for line in json.loads(response.read()):
            data.append(line["rezultat"])
        if data:
            return render_template('type/type.html', data=data[0])
        else:
            return render_template('type/type.html')
