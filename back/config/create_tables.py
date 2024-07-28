from database import engine, Base
from models import User

# Créer toutes les tables définies dans les modèles
Base.metadata.create_all(bind=engine)
