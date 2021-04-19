from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


employeeLogin = Blueprint("employeeLogin", __name__, template_folder="templates")

@employeeLogin.route('/employeeLogin')
def hireIntern1():
    return render_template('1hireIntern.html')

