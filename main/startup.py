def startup():
    render_template('startup.html')
    startup = Virtualstartup.query.all()
    return render_template('startup.html',startup = startup)