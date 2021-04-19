def login():
    return render_template('login.html')

def check():
    if request.method =="POST":
        email = request.form.get('email')
        password = request.form.get('pass')

        person = User.query.filter_by(emailid = email).first()
        if person.password == password:
            return redirect(url_for('startup'))    
        else:
            return render_template('login.html')