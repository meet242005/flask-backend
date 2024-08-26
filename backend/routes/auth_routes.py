from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from settings.auth_utils import get_user_by_email, create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if get_user_by_email(email):
            return jsonify({"msg": "User already exists"}), 400

        create_user(email, password)
        access_token = create_access_token(identity={"email": email})
        return jsonify(access_token=access_token), 200
    
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = get_user_by_email(email)
        if not user or not user.verify_password(password):
            return jsonify({"msg": "Bad email or password"}), 401

        access_token = create_access_token(identity={"email": email})
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
