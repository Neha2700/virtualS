from flask import Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()


ecreatestartup2 = Blueprint("ecreatestartup2", __name__, template_folder="templates")

@ecreatestartup2.route('/')
def createStartup2():
    return render_template('create startup2.html')

@ecreatestartup2.route('/create startup2', methods = ["POST"])
def store2():
    if request.method =="POST":
        vs_industry = request.form.get('industry')
        vs_project_nature = request.form.get('projectNature')
        vs_skills_required = request.form.get('skillsRequired')
        vs_technologies = request.form.get('technology')
        vs_id = db.session.query(Virtualstartup).count()
        counter =  vs_id +1

        admin = Virtualstartup.query.filter_by(vs_id=vs_id).first()

        admin.vs_industry = vs_industry
        admin.vs_technologies = vs_technologies
        admin.vs_skills_required = vs_skills_required
        db.session.commit()

        return redirect(url_for('manageStartup'))
