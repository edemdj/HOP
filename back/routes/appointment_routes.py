from flask import Blueprint, request, jsonify
from app import db
from models.appointment import Appointment

bp_appointments = Blueprint('appointments', __name__)

@bp_appointments.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.json
    new_appointment = Appointment(patient_id=data['patient_id'], professionnel_id=data['professionnel_id'], date=data['date'])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment added"}), 201

@bp_appointments.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    appointment = Appointment.query.get(id)
    if appointment is None:
        return jsonify({"message": "Appointment not found"}), 404
    return jsonify({"id": appointment.id, "patient_id": appointment.patient_id, "professionnel_id": appointment.professionnel_id, "date": appointment.date}), 200
