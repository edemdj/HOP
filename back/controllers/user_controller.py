from flask import Blueprint, request, jsonify

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/', methods=['POST'])
def add_user():
    from services.user_service import create_user  # Moved inside the function
    data = request.get_json()
    return create_user(data)

@users_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    from services.user_service import get_user_by_id  # Moved inside the function
    return get_user_by_id(id)

@users_bp.route('/<int:id>', methods=['PUT'])
def update_user_route(id):
    from services.user_service import update_user  # Moved inside the function
    data = request.get_json()
    return update_user(id, data)

@users_bp.route('/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    from services.user_service import delete_user  # Moved inside the function
    return delete_user(id)

@users_bp.route('/', methods=['GET'])
def get_all_users_route():
    from services.user_service import get_all_users  # Moved inside the function
    return get_all_users()
