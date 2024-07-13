from models import Patient
from app import db

def create_patient(data):
    new_patient = Patient(name=data['name'], date_of_birth=data['date_of_birth'])
    db.session.add(new_patient)
    db.session.commit()
    return {'message': 'Patient created successfully'}, 201

def get_patient_by_id(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return {'message': 'Patient not found'}, 404
    return {'name': patient.name, 'date_of_birth': patient.date_of_birth}, 200

def update_patient(patient_id, data):
    patient = Patient.query.get(patient_id)
    if not patient:
        return {'message': 'Patient not found'}, 404
    patient.name = data.get('name', patient.name)
    patient.date_of_birth = data.get('date_of_birth', patient.date_of_birth)
    db.session.commit()
    return {'message': 'Patient updated successfully'}, 200

def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return {'message': 'Patient not found'}, 404
    db.session.delete(patient)
    db.session.commit()
    return {'message': 'Patient deleted successfully'}, 200

def get_all_patients():
    patients = Patient.query.all()
    return [{'name': patient.name, 'date_of_birth': patient.date_of_birth} for patient in patients], 200
