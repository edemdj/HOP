from flask import Blueprint, request, jsonify
from app import db
from models.professional import Professionnel

bp_professionnels = Blueprint('professionnels', __name__)

@bp_professionnels.route('/professionnels', methods=['POST'])
def add_professionnel():
    data = request.json
    new_professionnel = Professionnel(name=data['name'], email=data['email'], profession=data['profession'])
    db.session.add(new_professionnel)
    db.session.commit()
    return jsonify({"message": "Professionnel added"}), 201

@bp_professionnels.route('/professionnels/<int:id>', methods=['GET'])
def get_professionnel(id):
    professionnel = Professionnel.query.get(id)
    if professionnel is None:
        return jsonify({"message": "Professionnel not found"}), 404
    return jsonify({"id": professionnel.id, "name": professionnel.name, "email": professionnel.email, "profession": professionnel.profession}), 200
