from app import app
from flask import render_template, Blueprint

generic_bp = Blueprint('generic', __name__)


@generic_bp.route("/")
def index():
    return render_template("index.html")
