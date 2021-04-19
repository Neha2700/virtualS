from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iStartupPage = Blueprint("iStartupPage", __name__, template_folder="templates")
@iStartupPage.route("/")
def intern-startupPage():
    return render_template('intern6StartupPage.html')
