from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import validates
from config.database import db

class Professional(db.Model):
    __tablename__ = 'professionals'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    specialization = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    def __init__(self, first_name, last_name, email, specialization, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.specialization = specialization
        self.date_of_birth = date_of_birth

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Invalid email address")
        return address

    # Getters and setters
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name cannot be empty")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        if not value:
            raise ValueError("Specialization cannot be empty")
        self._specialization = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value
