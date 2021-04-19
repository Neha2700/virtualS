from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


iSignup2 = Blueprint("iSignup2", __name__, template_folder="templates")
@iSignup2.route("/")
def internSignup2():
    return render_template('intern4-signup2.html')
