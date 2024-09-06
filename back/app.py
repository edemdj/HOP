from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)

# Route pour les patients
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = db.session.query(patients).all()  # Exemple d'utilisation de SQLAlchemy
    return jsonify([patient.to_dict() for patient in patients])

if __name__ == '__main__':
    app.run(debug=True)
