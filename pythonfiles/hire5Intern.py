
from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


hire5Intern = Blueprint("hire5Intern", __name__, template_folder="templates")

@hire5Intern.route('/')
def hireIntern5():
    return render_template('5hireIntern.html')
    

