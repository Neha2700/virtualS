from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iStartupList = Blueprint("iStartupList", __name__, template_folder="templates")
@iStartupList.route("/")
def intern-startupList():
    return render_template('intern5startupList.html')
