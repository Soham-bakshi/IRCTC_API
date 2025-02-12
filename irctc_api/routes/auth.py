from flask import Blueprint, request, jsonify
from app import db, bcrypt, jwt
from models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password_hash=hashed_password, role=data.get('role', 'user'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        # ✅ FIXED: Use user.id as identity (string)
        access_token = create_access_token(identity=str(user.id), additional_claims={"username": user.username, "role": user.role})
        return jsonify({'access_token': access_token})
    return jsonify({'message': 'Invalid credentials'}), 401


