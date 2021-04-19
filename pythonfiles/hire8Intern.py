

from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire8Intern = Blueprint("hire8Intern", __name__, template_folder="templates")

@hire8Intern.route('/')
def hireIntern8():
    return render_template('8hireIntern.html')

