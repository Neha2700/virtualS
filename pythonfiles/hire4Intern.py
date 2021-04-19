from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire4Intern = Blueprint("hire4Intern", __name__, template_folder="templates")

@hire4Intern.route('/')
def hireIntern4():
    return render_template('4hireIntern.html')

