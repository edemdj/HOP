from flask import Flask
from config.database import engine, Base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Créez la base de données
Base.metadata.create_all(bind=engine)

# Enregistrement des Blueprints (importez après la création de l'app)
from controllers.user_controller import users_bp
from controllers.patient_controller import patients_bp
from controllers.professionals_controller import professionals_bp

app.register_blueprint(users_bp, url_prefix='/api/users')
app.register_blueprint(patients_bp, url_prefix='/api/patients')
app.register_blueprint(professionals_bp, url_prefix='/api/professionals')

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

if __name__ == '__main__':
    app.run(debug=True)
