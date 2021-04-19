from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire2Intern = Blueprint("hire2Intern", __name__, template_folder="templates")

@hire2Intern.route('/')
def hireIntern2():
    return render_template('2hireIntern.html')
