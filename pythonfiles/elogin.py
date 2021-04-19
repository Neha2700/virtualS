from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


elogin = Blueprint("elogin", __name__, template_folder="templates")

@elogin.route('/')
def login():
    return render_template('login.html')

@elogin.route('/' , methods = ['POST'])
def check():
    if request.method =="POST":
        email = request.form.get('email')
        password = request.form.get('pass')

        person = User.query.filter_by(emailid = email).first()
        if person.password == password:
            return redirect(url_for('ecreatestartup.startup'))    
        else:
            return render_template('login.html')
