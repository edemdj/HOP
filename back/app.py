from flask import Flask
from controllers.user_controller import users_bp
from controllers.patient_controller import patients_bp
from controllers.professionals_controller import professionals_bp
from config.database import engine, Base
from sqlalchemy.orm import sessionmaker

# Création de l'application Flask
app = Flask(__name__)

# Enregistrement des Blueprints
app.register_blueprint(users_bp, url_prefix='/api')
app.register_blueprint(patients_bp, url_prefix='/api')
app.register_blueprint(professionals_bp, url_prefix='/api')

# Création de la base de données
Base.metadata.create_all(bind=engine)

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

# Démarrage de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
