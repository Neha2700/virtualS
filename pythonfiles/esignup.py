from flask import Flask, Blueprint, render_template ,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from pythonfiles.models import *
db=SQLAlchemy()

esignup = Blueprint("esignup", __name__, template_folder="templates")

@esignup.route('/' , methods = ['POST'])
   
def insert():
    if request.method =="POST":
        name = request.form['name']    
        email = request.form['email']  
        phone = request.form['phone']  
        password = request.form['psw'] 
        user_id = db.session.query(User).count()
        global_user = user_id
        counter =  user_id +1

        user_obj = User(user_id = counter,name =name,password = password,emailid = email,phone=phone)
        db.session.add(user_obj)
        db.session.commit()
        return redirect(url_for('elogin.login'))

@esignup.route('/')
def signup():
    return render_template('signup.html')

