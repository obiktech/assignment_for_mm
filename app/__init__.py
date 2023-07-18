from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from .utils import error_handlers
import os
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv(".env")

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
from .routes import admin, employee
from .views import generic_bp

app.register_blueprint(employee.employee_bp)
app.register_blueprint(admin.admin_bp)
app.register_blueprint(generic_bp)
mail = Mail(app)


error_handlers(app)
