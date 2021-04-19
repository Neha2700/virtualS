from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iSignup1 = Blueprint("iSignup1", __name__, template_folder="templates")

@iSignup1.route("/")
def internSignup1():
    return render_template('intern3-signup1.html')
