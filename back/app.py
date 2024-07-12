from config.database import Base, engine
from models.patient import Patient
from models.professional import Professional

# Crée les tables dans la base de données
Base.metadata.create_all(bind=engine)

print("Les tables ont été créées avec succès")
