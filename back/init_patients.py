from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:edem1234@localhost/hop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

def init_db():
    with app.app_context():
        db.create_all()
        patients = [
            Patient(name='John Doe', email='john.doe@example.com', age=30),
            Patient(name='Jane Smith', email='jane.smith@example.com', age=25),
            Patient(name='Alice Johnson', email='alice.johnson@example.com', age=40),
            Patient(name='Bob Brown', email='bob.brown@example.com', age=35),
            Patient(name='Carol Davis', email='carol.davis@example.com', age=50),
            Patient(name='David Wilson', email='david.wilson@example.com', age=45)
        ]
        for patient in patients:
            db.session.add(patient)
        db.session.commit()
        print("Base de données initialisée avec succès")

if __name__ == '__main__':
    init_db()
