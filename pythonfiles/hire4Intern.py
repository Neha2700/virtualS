from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


empViewExistApplAndSearch = Blueprint("empViewExistApplAndSearch", __name__, template_folder="templates")
@empViewExistApplAndSearch.route('/')
def hireIntern4():
    return render_template('4hireIntern.html')

