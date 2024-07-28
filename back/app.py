from flask import Flask
from config.database import db, init_app
from models.professional import Professional
from models.patient import Patient
from models.appointment import Appointment
from models.user import User

app = Flask(__name__)

init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
