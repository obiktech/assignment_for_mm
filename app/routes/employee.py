from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import os
from werkzeug.utils import secure_filename
from app import db, bcrypt
from app.models import User
from app.utils.authentication import register_employee, login_emp
employee_bp = Blueprint('employee', __name__, url_prefix="/auth")


@employee_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    ret = register_employee(email, password)
    if ret == 1:

        return jsonify({'message': 'Email already registered'}), 400

    elif ret == 2:
        return jsonify({'message': 'Invalid email '}), 400

    # Send confirmation email
    # ...
    elif ret == 0:

        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'message': 'Invalid data '}), 400


@employee_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    ret = login_emp(email, password)
    if ret == 1:
        return jsonify({'message': 'Invalid credentials'}), 401
    if ret == 2:
        return jsonify({'message': 'User Does Not exist'}), 401

    else:
        return jsonify({'access_token': ret}), 200


ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@employee_bp.route('/upload-profile-picture', methods=['POST'])
@jwt_required()
def upload_profile_picture():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('path_to_profile_picture_directory', filename))
        user.profile_picture = filename
        db.session.commit()
        return jsonify({'message': 'Profile picture uploaded successfully'}), 200

    return jsonify({'message': 'Invalid file format'}), 400
