from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empSearchIntern2 = Blueprint("empSearchIntern2", __name__, template_folder="templates")
@empSearchIntern2.route('/employeeLogin-SearchInterns2')
def hireIntern6():
    return render_template('6hireIntern.html')

