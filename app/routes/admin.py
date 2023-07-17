from flask import Blueprint, request, jsonify
from flask_bcrypt import check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    if not current_user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403

    return jsonify({'message': 'Welcome Admin!'}), 200
