from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_user_by_id, update_user, delete_user, get_all_users

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    response, status_code = create_user(data)
    return jsonify(response), status_code

@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user_route(id):
    response, status_code = get_user_by_id(id)
    return jsonify(response), status_code

@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user_route(id):
    data = request.get_json()
    response, status_code = update_user(id, data)
    return jsonify(response), status_code

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    response, status_code = delete_user(id)
    return jsonify(response), status_code

@users_bp.route('/users', methods=['GET'])
def get_users_route():
    response, status_code = get_all_users()
    return jsonify(response), status_code
