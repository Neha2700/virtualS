from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empViewExistAppl = Blueprint("empViewExistAppl", __name__, template_folder="templates")

@empViewExistAppl.route('/employeeLogin-ViewExistingApplications ')
def hireIntern3():
    return render_template('3hireIntern.html')

