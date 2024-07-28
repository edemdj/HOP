from sqlalchemy.orm import sessionmaker
from config.database import engine
from models import Professional

# Créer une session
Session = sessionmaker(bind=engine)
session = Session()

# Définir les professionnels
professionals = [
    Professional(name='John Doe', email='john@example.com', phone='1234567890', profession='Engineer', address='123 Main St', company='Tech Corp'),
    Professional(name='Jane Smith', email='jane@example.com', phone='2345678901', profession='Doctor', address='456 Elm St', company='Health Inc'),
    Professional(name='Jim Brown', email='jim@example.com', phone='3456789012', profession='Architect', address='789 Pine St', company='Build LLC'),
    Professional(name='Sara White', email='sara@example.com', phone='4567890123', profession='Lawyer', address='101 Maple St', company='Law Firm'),
    Professional(name='Tom Green', email='tom@example.com', phone='5678901234', profession='Teacher', address='202 Oak St', company='Edu Group'),
    Professional(name='Emma Blue', email='emma@example.com', phone='6789012345', profession='Artist', address='303 Birch St', company='Art Studio')
]

# Ajouter les professionnels à la session
session.add_all(professionals)

# Commiter les changements
session.commit()

print("Professionals inserted successfully!")
