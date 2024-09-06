from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:edem1234@localhost/hop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Professionnel(db.Model):
    __tablename__ = 'professionnels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    profession = db.Column(db.String(50), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()
        professionals = [
            {"name": "Alice Smith", "email": "alice@example.com", "profession": "Doctor"},
            {"name": "Bob Johnson", "email": "bob@example.com", "profession": "Lawyer"},
            {"name": "Charlie Brown", "email": "charlie@example.com", "profession": "Teacher"}
        ]
        for prof in professionals:
            new_professional = Professionnel(name=prof['name'], email=prof['email'], profession=prof['profession'])
            db.session.add(new_professional)
        db.session.commit()
        print("Base de données initialisée avec succès")

if __name__ == '__main__':
    init_db()
