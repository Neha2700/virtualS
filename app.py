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

@app.route('/manage startup.html')
def manageStartup():
    return render_template('manage startup.html')










    


             



if __name__ == "__main__":
    app.run(debug=True)