from flask import Blueprint, request, jsonify
from services.appointment_service import create_appointment, get_appointment_by_id, update_appointment, delete_appointment, get_all_appointments

appointments_bp = Blueprint('appointments_bp', __name__)

@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment_route():
    data = request.get_json()
    response, status_code = create_appointment(data)
    return jsonify(response), status_code

@appointments_bp.route('/appointments/<int:id>', methods=['GET'])
def get_appointment_route(id):
    response, status_code = get_appointment_by_id(id)
    return jsonify(response), status_code

@appointments_bp.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment_route(id):
    data = request.get_json()
    response, status_code = update_appointment(id, data)
    return jsonify(response), status_code

@appointments_bp.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment_route(id):
    response, status_code = delete_appointment(id)
    return jsonify(response), status_code

@appointments_bp.route('/appointments', methods=['GET'])
def get_appointments_route():
    response, status_code = get_all_appointments()
    return jsonify(response), status_code
