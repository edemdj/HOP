from models import Professionnel
from app import db

def create_professionnel(data):
    new_professionnel = Professionnel(name=data['name'], specialization=data['specialization'])
    db.session.add(new_professionnel)
    db.session.commit()
    return {'message': 'Professionnel created successfully'}, 201

def get_professionnel_by_id(professionnel_id):
    professionnel = Professionnel.query.get(professionnel_id)
    if not professionnel:
        return {'message': 'Professionnel not found'}, 404
    return {'name': professionnel.name, 'specialization': professionnel.specialization}, 200

def update_professionnel(professionnel_id, data):
    professionnel = Professionnel.query.get(professionnel_id)
    if not professionnel:
        return {'message': 'Professionnel not found'}, 404
    professionnel.name = data.get('name', professionnel.name)
    professionnel.specialization = data.get('specialization', professionnel.specialization)
    db.session.commit()
    return {'message': 'Professionnel updated successfully'}, 200

def delete_professionnel(professionnel_id):
    professionnel = Professionnel.query.get(professionnel_id)
    if not professionnel:
        return {'message': 'Professionnel not found'}, 404
    db.session.delete(professionnel)
    db.session.commit()
    return {'message': 'Professionnel deleted successfully'}, 200

def get_all_professionnels():
    professionnels = Professionnel.query.all()
    return [{'name': professionnel.name, 'specialization': professionnel.specialization} for professionnel in professionnels], 200
