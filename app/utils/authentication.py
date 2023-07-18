from app.models import User
from flask_bcrypt import generate_password_hash, check_password_hash
from app import db
from flask_jwt_extended import create_access_token
from app.utils.services import send_email

def register_employee(email, password):
    if User.query.filter_by(email=email).first():
        return 1
    if "@" not in email:
        return 2
    if password == "":
        return 3

    hashed_password = generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    send_email(email)

    return 0


def login_emp(email, password):
    user = User.query.filter_by(email=email)

    if (user.count == 0):
        return 2
    user = user.first()

    if not user or not check_password_hash(user.password, password):
        return 1

    access_token = create_access_token(identity=user.id)
    return access_token


def reset_password(user_id):
    user = User.query.get(user_id)