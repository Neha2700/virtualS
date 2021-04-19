from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire7Intern = Blueprint("hire7Intern", __name__, template_folder="templates")

@hire7Intern.route('/')
def hireIntern7():
    return render_template('7hireIntern.html')