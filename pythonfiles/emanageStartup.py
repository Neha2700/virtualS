from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


emanageStartup = Blueprint("emanageStartup", __name__, template_folder="templates")

@emanageStartup.route("/")
def manageStartup():
    return render_template('manage startup.html')