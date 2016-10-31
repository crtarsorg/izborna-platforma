from flask import Blueprint
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    return render_template('site/home.html', static_folder='static', template_folder='templates')
