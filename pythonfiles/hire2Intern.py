from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


employeeLoginHireMember = Blueprint("/employeeLogin-HireMember", __name__, template_folder="templates")

@employeeLoginHireMember.route('/')
def hireIntern2():
    return render_template('2hireIntern.html')

