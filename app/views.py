from app import app
from flask import render_template, Blueprint, request
from flask_jwt_extended import jwt_required
generic_bp = Blueprint('generic', __name__)


@generic_bp.route("/")
def index():
    print(request.headers)
    token = request.headers["Authorization"]
    print(token)
    return render_template("profile.html")




@generic_bp.route("/login", methods=["GET", "POST"])
def loginpage():

    if request.method == "POST":
        print("postmethod")
    return render_template("loginpage.html")
