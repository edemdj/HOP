from database import SessionLocal
from models import User

def create_user(username: str, email: str):
    # Créer une nouvelle session
    db = SessionLocal()
    try:
        # Créer un nouvel utilisateur
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        db.close()

# Exemple d'utilisation
if __name__ == "__main__":
    new_user = create_user("JeanDupont", "jean.dupont@example.com")
    if new_user:
        print(f"Utilisateur créé : {new_user.username}, {new_user.email}")
