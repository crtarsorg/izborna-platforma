# coding=utf-8
import pprint

from flask import Blueprint,request, redirect,url_for, flash
from flask import render_template
import json,urllib

from flask_mail import Message
from app import mail

mod_contact = Blueprint('contact', __name__, url_prefix="/<lang_code>/contact",static_folder="static", template_folder='templates', )
#get data for all territories selected by year

@mod_contact.route('/', methods=['GET'])
def contact_page():
    return render_template('contact/contact.html',year=0)

@mod_contact.route('/sendemail', methods=['POST'])
def send_email():
    data=request.form.to_dict()
    print data
    message ="from:" + data['email'] + '<br/>' + data['Message'] + '/n '
    msg = Message(subject=data['subject'],
                  sender=data['Name'],
                  recipients=["kontakt@gradjaninastrazi.rs"],
                  body=message)
    msg.html="<b>From:</b> " + data['email'] + '<br/><br/>' + data['Message']
    mail.send(msg)
    flash('Порука је успешно послата')
    return redirect(url_for('contact.contact_page'))



