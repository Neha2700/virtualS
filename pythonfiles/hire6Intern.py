
from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire6Intern = Blueprint("hire6Intern", __name__, template_folder="templates")

@hire6Intern.route('/')
def hireIntern6():
    return render_template('6hireIntern.html')

