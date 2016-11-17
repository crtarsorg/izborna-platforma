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
        url2014 = "http://0.0.0.0:5006/api/izbori/2/parlamentarni/godina/2014/instanca/4"
        response = urllib.urlopen(url2014)
        for line in json.loads(response.read()):
            data.append(line)
        print data
        if data:
            return render_template('type/type.html', data=data[0])
        else:
            return render_template('type/type.html')
