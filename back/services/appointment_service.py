# gestion des rendez-vous
from models import Appointment
from app import db

def create_appointment(data):
    new_appointment = Appointment(patient_id=data['patient_id'], professionnel_id=data['professionnel_id'], appointment_date=data['appointment_date'])
    db.session.add(new_appointment)
    db.session.commit()
    return {'message': 'Appointment created successfully'}, 201

def get_appointment_by_id(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return {'message': 'Appointment not found'}, 404
    return {
        'patient_id': appointment.patient_id,
        'professionnel_id': appointment.professionnel_id,
        'appointment_date': appointment.appointment_date
    }, 200

def update_appointment(appointment_id, data):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return {'message': 'Appointment not found'}, 404
    appointment.patient_id = data.get('patient_id', appointment.patient_id)
    appointment.professionnel_id = data.get('professionnel_id', appointment.professionnel_id)
    appointment.appointment_date = data.get('appointment_date', appointment.appointment_date)
    db.session.commit()
    return {'message': 'Appointment updated successfully'}, 200

def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return {'message': 'Appointment not found'}, 404
    db.session.delete(appointment)
    db.session.commit()
    return {'message': 'Appointment deleted successfully'}, 200

def get_all_appointments():
    appointments = Appointment.query.all()
    return [
        {
            'patient_id': appointment.patient_id,
            'professionnel_id': appointment.professionnel_id,
            'appointment_date': appointment.appointment_date
        } for appointment in appointments
    ], 200
