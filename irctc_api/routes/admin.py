from flask import Blueprint, request, jsonify
from app import db
from models.train import Train

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/trains', methods=['POST'])
def add_train():
    if request.headers.get('API-KEY') != os.getenv("ADMIN_API_KEY"):
        return jsonify({'message': 'Unauthorized'}), 403
    data = request.json
    train = Train(train_name=data['train_name'], source=data['source'], destination=data['destination'], total_seats=data['total_seats'], available_seats=data['total_seats'])
    db.session.add(train)
    db.session.commit()
    return jsonify({'message': 'Train added successfully'})

