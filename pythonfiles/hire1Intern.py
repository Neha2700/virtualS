from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire1Intern = Blueprint("hire1Intern", __name__, template_folder="templates")

@hire1Intern.route('/')

def hireIntern1():
    return render_template('1hireIntern.html')

