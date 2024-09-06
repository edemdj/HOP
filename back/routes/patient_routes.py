from flask import Blueprint, request, jsonify
from app import app, db
from models.patient import Patient

bp_patients = Blueprint('patients', __name__)

@bp_patients.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    new_patient = Patient(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added"}), 201

@bp_patients.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({"message": "Patient not found"}), 404
    return jsonify({"id": patient.id, "name": patient.name, "email": patient.email, "age": patient.age}), 200
