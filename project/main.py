from flask import Blueprint, Flask ,render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/hotel')
@login_required
def hotel():
    return render_template("contentsHotel.html", name = current_user.name)