from datetime import datetime
from config.database import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)

class Professionnel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialization = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    professionnel_id = db.Column(db.Integer, db.ForeignKey('professionnel.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    patient = db.relationship('Patient', backref=db.backref('appointments', lazy=True))
    professionnel = db.relationship('Professionnel', backref=db.backref('appointments', lazy=True))
