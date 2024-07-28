from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crée une instance de SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    # Configure l'app Flask avec l'URL de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactiver les notifications de modification pour économiser des ressources
    db.init_app(app)
