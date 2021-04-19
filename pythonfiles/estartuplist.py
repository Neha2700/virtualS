from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
import pythonfiles.estartuplist
import pythonfiles.elogin


db=SQLAlchemy()


estartuplist = Blueprint("ecreatestartup", __name__, template_folder="templates")

@estartuplist.route('/')
def startup():
    render_template('startup.html')
    startup = Virtualstartup.query.filter_by(founder_id = pythonfiles.elogin.global_user)
    return render_template('startup.html',startup = startup)
