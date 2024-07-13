import re
from datetime import datetime
from utils.constants import DATE_FORMAT

def validate_email(email):
    """Valide si l'email a un format correct."""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return False

def validate_date(date_string):
    """Valide si la date a un format correct."""
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False

def validate_password(password):
    """Valide si le mot de passe est suffisamment fort."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
