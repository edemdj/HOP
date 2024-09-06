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

def check_professionals():
    with app.app_context():
        professionals = Professionnel.query.all()
        for professional in professionals:
            print(f'ID: {professional.id}, Name: {professional.name}, Email: {professional.email}, Profession: {professional.profession}')

if __name__ == '__main__':
    check_professionals()
