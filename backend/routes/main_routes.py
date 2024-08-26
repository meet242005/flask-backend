from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from settings.auth_utils import get_user_by_email

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return {"message": "Welcome to the Lit-Coders Backend!"}

@main_bp.route('/verify_token',methods=['POST'])
@jwt_required()
def verify_token():
    current_user = get_jwt_identity()
    email = current_user["email"]
    user = get_user_by_email(email)
    return jsonify({"user": user.to_dict()}), 200
