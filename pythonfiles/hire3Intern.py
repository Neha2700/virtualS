from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire3Intern = Blueprint("hire3Intern", __name__, template_folder="templates")

@hire3Intern.route('/')
def hireIntern3():
    return render_template('3hireIntern.html')

