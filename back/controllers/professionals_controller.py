from flask import Blueprint, request, jsonify
from back.services.professionnel_service import create_professionnel, get_professionnel_by_id, update_professionnel, delete_professionnel, get_all_professionnels

professionnels_bp = Blueprint('professionnels_bp', __name__)

@professionnels_bp.route('/professionnels', methods=['POST'])
def create_professionnel_route():
    data = request.get_json()
    response, status_code = create_professionnel(data)
    return jsonify(response), status_code

@professionnels_bp.route('/professionnels/<int:id>', methods=['GET'])
def get_professionnel_route(id):
    response, status_code = get_professionnel_by_id(id)
    return jsonify(response), status_code

@professionnels_bp.route('/professionnels/<int:id>', methods=['PUT'])
def update_professionnel_route(id):
    data = request.get_json()
    response, status_code = update_professionnel(id, data)
    return jsonify(response), status_code

@professionnels_bp.route('/professionnels/<int:id>', methods=['DELETE'])
def delete_professionnel_route(id):
    response, status_code = delete_professionnel(id)
    return jsonify(response), status_code

@professionnels_bp.route('/professionnels', methods=['GET'])
def get_professionnels_route():
    response, status_code = get_all_professionnels()
    return jsonify(response), status_code
