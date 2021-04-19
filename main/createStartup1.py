def createStartup1():
    return render_template('create startup1.html')

def store():
    if request.method =="POST":
        vs_title = request.form["title"]
        vs_pain = request.form["pain"]
        vs_solution = request.form["solution"]
        vs_id = db.session.query(Virtualstartup).count()
        counter =  vs_id +1

        startupObj = Virtualstartup( founder_id = global_user, vs_id = counter,vs_name =vs_title,vs_pain_areas = vs_pain,vs_solution = vs_solution)
        db.session.add(startupObj)
        db.session.commit()
        return redirect(url_for('createStartup2'))  