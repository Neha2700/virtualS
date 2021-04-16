from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session

db = SQLAlchemy()

class User(db.Model):
    """ User model """

    __table__name ="user"
    user_id = db.Column(db.Integer,primary_key =True) 
    role_id = db.Column(db.Integer)
    name = db.Column(db.String(25),nullable =False)
    emailid = db.Column(db.String(),nullable =False)
    phone = db.Column(db.Integer,nullable = False)
    password = db.Column(db.String(),nullable =False)
    last_update = db.Column(db.Integer)
    updatedby_id = db.Column(db.Integer)

class Virtualstartup(db.Model):
    """   """    
    __table__name = "virtualstartup"
    vs_id = db.Column(db.Integer,primary_key =True) 
    founder_id = db.Column(db.Integer)
    vs_name = db.Column(db.String,nullable = False) 
    vs_pain_areas = db.Column(db.String,nullable = False) 
    vs_solution = db.Column(db.String()) 
    vs_industry = db.Column(db.String()) 
    vs_skills_required = db.Column(db.String()) 
    vs_technologies = db.Column(db.String()) 
    last_updated = db.Column(db.String()) 
    updatedby_id = db.Column(db.String()) 
    