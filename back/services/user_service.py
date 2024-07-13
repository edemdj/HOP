from models import User
from app import db

def create_user(data):
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User created successfully'}, 201

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    return {'username': user.username, 'email': user.email}, 200

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return {'message': 'User updated successfully'}, 200

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404
    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted successfully'}, 200

def get_all_users():
    users = User.query.all()
    return [{'username': user.username, 'email': user.email} for user in users], 200
