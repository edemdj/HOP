from flask import Blueprint, request, jsonify
from services.patient_service import create_patient, get_patient_by_id, update_patient, delete_patient, get_all_patients

patients_bp = Blueprint('patients_bp', __name__)

@patients_bp.route('/patients', methods=['POST'])
def create_patient_route():
    data = request.get_json()
    response, status_code = create_patient(data)
    return jsonify(response), status_code

@patients_bp.route('/patients/<int:id>', methods=['GET'])
def get_patient_route(id):
    response, status_code = get_patient_by_id(id)
    return jsonify(response), status_code

@patients_bp.route('/patients/<int:id>', methods=['PUT'])
def update_patient_route(id):
    data = request.get_json()
    response, status_code = update_patient(id, data)
    return jsonify(response), status_code

@patients_bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient_route(id):
    response, status_code = delete_patient(id)
    return jsonify(response), status_code

@patients_bp.route('/patients', methods=['GET'])
def get_patients_route():
    response, status_code = get_all_patients()
    return jsonify(response), status_code
