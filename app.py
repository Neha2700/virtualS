from flask import Flask, render_template , request ,redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
from datetime import datetime


from pythonfiles.elanding import elanding
from pythonfiles.elogin import elogin
from pythonfiles.esignup import esignup
from pythonfiles.estartuplist import estartuplist
from pythonfiles.ecreatestartup1 import ecreatestartup1
from pythonfiles.ecreatestartup2 import ecreatestartup2
from pythonfiles.emanageStartup import emanageStartup

from pythonfiles.intern1Landing import iLanding
from pythonfiles.intern2login import iLogin
from pythonfiles.intern3Signup1 import iSignup1
from pythonfiles.intern4Signup2 import iSignup2
from pythonfiles.intern5startupList import iStartupList
from pythonfiles.intern6StartupPage import iStartupPage

from pythonfiles.hire1Intern import hireIntern1
from pythonfiles.hire2Intern import hireIntern2
from pythonfiles.hire3Intern import hireIntern3
from pythonfiles.hire4Intern import hireIntern4
from pythonfiles.hire5Intern import hireIntern5
from pythonfiles.hire6Intern import hireIntern6
from pythonfiles.hire7Intern import hireIntern7
from pythonfiles.hire8Intern import hireIntern8

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost/vsp'
db=SQLAlchemy(app)
# db.init_app(app)

app.register_blueprint(elanding, url_prefix="/")
app.register_blueprint(elogin ,url_prefix="/login")
app.register_blueprint(esignup ,url_prefix="/signup")
app.register_blueprint(estartuplist ,url_prefix="/startup")
app.register_blueprint(ecreatestartup1 ,url_prefix="/create startup1")
app.register_blueprint(ecreatestartup2 ,url_prefix="/create startup2")
app.register_blueprint(emanageStartup, url_prefix="/manage startup")
app.register_blueprint(iLanding, url_prefix="/intern landing")
app.register_blueprint(iLogin, url_prefix="/intern login")
app.register_blueprint(iSignup1, url_prefix="/intern signup1")
app.register_blueprint(iSignup2, url_prefix="/intern signup2")
app.register_blueprint(iStartupList, url_prefix="/intern startupList")
app.register_blueprint(iStartupPage, url_prefix="/intern startupPage")
app.register_blueprint(employeeLogin, url_prefix="/employeeLogin")
app.register_blueprint(employeeLoginHireMember, url_prefix="/employee login hire member")
app.register_blueprint(empViewExistAppl, url_prefix="/employee View Existing Application")
app.register_blueprint(empViewExistApplAndSearch, url_prefix="/employee ViewExisting Appl and search")
app.register_blueprint(empSearchIntern, url_prefix="/employee-Search Intern")
app.register_blueprint(empSearchIntern2, url_prefix="/employee-Search Intern2")
app.register_blueprint(empSearchIntern2, url_prefix="employeeLogin-candidate search")
app.register_blueprint(empViewAppli, url_prefix="employeeLogin-view Application")


# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/signup' , methods = ['POST'])
   
# def insert():
#     if request.method =="POST":
#         name = request.form['name']    
#         email = request.form['email']  
#         phone = request.form['phone']  
#         password = request.form['psw'] 
#         user_id = db.session.query(User).count()
#         global_user = user_id
#         counter =  user_id +1

#         user_obj = User(user_id = counter,name =name,password = password,emailid = email,phone=phone)
#         db.session.add(user_obj)
#         db.session.commit()
#         return redirect(url_for('login.html'))
        

# @app.route('/startup')
# def startup():
#     render_template('startup.html')
#     startup = Virtualstartup.query.all()
#     return render_template('startup.html',startup = startup)

    

# @app.route('/startup', methods =["POST"])

# def check():
#     if request.method =="POST":
#         email = request.form.get('email')
#         password = request.form.get('pass')

#         person = User.query.filter_by(emailid = email).first()
#         if person.password == password:
#             return render_template('startup.html')
#         else:
#             return render_template('login.html')

# def startup():
#     startup = Virtualstartup.query.all()
#     # startup = session.query(VirtualStartup).first()
#     # print(startup.vs_name)
#     # startup = Virtualstartup.query.filter_by(founder_id=1).first()
#     return render_template('startup.html',startup = startup)

    


     

# @app.route('/create startup1')
# def createStartup1():
#     return render_template('create startup1.html')

# @app.route('/create startup1' , methods = ["POST"])
# def store():
#     if request.method =="POST":
#         vs_title = request.form["title"]
#         vs_pain = request.form["pain"]
#         vs_solution = request.form["solution"]
#         vs_id = db.session.query(Virtualstartup).count()
#         counter =  vs_id +1

#         startupObj = Virtualstartup( founder_id = global_user, vs_id = counter,vs_name =vs_title,vs_pain_areas = vs_pain,vs_solution = vs_solution)
#         db.session.add(startupObj)
#         db.session.commit()
#         return redirect(url_for('createStartup2'))    




# @app.route('/create startup2.html')
# def createStartup2():
#     return render_template('create startup2.html')

# @app.route('/create startup2', methods = ["POST"])
# def store2():
#     if request.method =="POST":
#         vs_industry = request.form.get('industry')
#         vs_project_nature = request.form.get('projectNature')
#         vs_skills_required = request.form.get('skillsRequired')
#         vs_technologies = request.form.get('technology')
#         vs_id = db.session.query(Virtualstartup).count()
#         counter =  vs_id +1

#         admin = Virtualstartup.query.filter_by(vs_id=vs_id).first()

#         admin.vs_industry = vs_industry
#         admin.vs_technologies = vs_technologies
#         admin.vs_skills_required = vs_skills_required
#         db.session.commit()

#         return redirect(url_for('manageStartup'))
   









# @app.route('/manage startup.html')
# def manageStartup():
#     return render_template('manage startup.html')

# @app.route('/login' , methods = ['POST'])
# def check():
#     if request.method =="POST":
#         email = request.form.get('email')
#         password = request.form.get('pass')

#         person = User.query.filter_by(emailid = email).first()
#         if person.password == password:
#             return redirect(url_for('startup'))    
#         else:
#             return render_template('login.html')











# ############################################
#     if request.method =="POST":
#         email = request.form.get('email')
#         password = request.form.get('pass')

#         person = User.query.filter_by(emailid = email).first()
#         if person.password == password:
#             return render_template('startup.html')
#         else:
    


             



if __name__ == "__main__":
    app.run(debug=True)