from flask import Blueprint

from .patient_routes import bp_patients
from .professional_routes import bp_professionnels
from .user_routes import bp_users
from .appointment_routes import bp_appointments

def register_routes(app):
    app.register_blueprint(bp_patients)
    app.register_blueprint(bp_professionnels)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_appointments)
