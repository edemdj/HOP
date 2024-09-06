from app import db, Patient
from app import app

def check_patients():
    with app.app_context():
        patients = Patient.query.all()
        for patient in patients:
            print(f'ID: {patient.id}, Name: {patient.name}, Email: {patient.email}, Age: {patient.age}')

if __name__ == '__main__':
    check_patients()
