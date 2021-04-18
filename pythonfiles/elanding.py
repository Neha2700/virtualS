from flask import Blueprint, render_template 


elanding = Blueprint("elanding", __name__, template_folder="templates")


@elanding.route('/')
def hello_world():
    return render_template('landing.html')
