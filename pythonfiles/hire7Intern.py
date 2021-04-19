from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empSearchIntern2 = Blueprint("empSearchIntern2", __name__, template_folder="templates")
@app.route('/')
def hireIntern7():
    return render_template('7hireIntern.html')

