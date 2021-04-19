from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iLogin = Blueprint("iLogin", __name__, template_folder="templates")
@iLogin.route("/")
def internLogin():
    return render_template('intern2Login.html')
