from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empSearchIntern = Blueprint("empSearchIntern", __name__, template_folder="templates")
@empSearchIntern.route('/employeeLogin-searchInterns')
def hireIntern5():
    return render_template('5hireIntern.html')

