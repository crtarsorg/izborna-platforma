# coding=utf-8
import pprint

from flask import Blueprint,request, redirect,url_for
from flask import render_template
from app import mongo_utils
from bson.json_util import dumps
import json,urllib
from bson import json_util
from flask_mail import Message
from app import mail

mod_contact = Blueprint('contact', __name__, url_prefix="/contact",static_folder="static", template_folder='templates', )
#get data for all territories selected by year
@mod_contact.route('/', methods=['GET'])
def contact_page():
    return render_template('contact/contact.html')

@mod_contact.route('/sendemail', methods=['POST'])
def send_email():
    data=request.form.to_dict()
    print data
    message = data['Message'] + '/n ' + "email:" + data['email']
    msg = Message(subject=data['subject'],
                  sender=data['Name'],
                  recipients=["feride_adili@hotmail.com"],
                  body=message)
    mail.send(msg)
    return redirect(url_for('contact.contact_page'))



