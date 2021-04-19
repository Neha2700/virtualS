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

from pythonfiles.hire1Intern import hire1Intern
from pythonfiles.hire2Intern import hire2Intern
from pythonfiles.hire3Intern import hire3Intern
from pythonfiles.hire4Intern import hire4Intern
from pythonfiles.hire5Intern import hire5Intern
from pythonfiles.hire6Intern import hire6Intern
from pythonfiles.hire7Intern import hire7Intern
from pythonfiles.hire8Intern import hire8Intern

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

app.register_blueprint(hire1Intern, url_prefix="/employee login")
app.register_blueprint(hire2Intern, url_prefix="/employeelogin-hireMember")
app.register_blueprint(hire3Intern, url_prefix="/employee View Existing Application")
app.register_blueprint(hire4Intern, url_prefix="/employee ViewExisting Appl and search")
app.register_blueprint(hire5Intern, url_prefix="/employee-Search Intern")
app.register_blueprint(hire6Intern, url_prefix="/employee-Search Intern2")
app.register_blueprint(hire7Intern, url_prefix="/employeeLogin-candidate search")
app.register_blueprint(hire8Intern, url_prefix="/employeeLogin-view Application")






if __name__ == "__main__":
    app.run(debug=True)