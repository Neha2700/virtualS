from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empViewAppli = Blueprint("empViewAppli", __name__, template_folder="templates")
@empViewAppli.route('/')
def hireIntern8():
    return render_template('8hireIntern.html')

