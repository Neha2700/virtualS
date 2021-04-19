from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iLanding = Blueprint("iLanding", __name__, template_folder="templates")

@iLanding.route("/")
def internLanding():
    return render_template('intern1Landing.html')

