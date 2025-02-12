from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.train import Train
from models.booking import Booking
from app import db

user_bp = Blueprint("user", __name__)

@user_bp.route('/book', methods=['POST'])
@jwt_required()
def book_seat():
    user_id = int(get_jwt_identity())  # Convert string ID back to integer
    user = User.query.get(user_id)  # Fetch user from DB

    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    train = Train.query.filter_by(id=data["train_id"]).first()

    if not train or train.available_seats <= 0:
        return jsonify({"message": "No seats available"}), 400

    train.available_seats -= 1

    new_booking = Booking(user_id=user.id, train_id=train.id, seat_number=train.total_seats - train.available_seats)
    db.session.add(new_booking)

    try:
        db.session.commit()  # ✅ Commit changes inside the try block
        return jsonify({"message": "Seat booked successfully", "booking_id": new_booking.id})
    except:
        db.session.rollback()
        return jsonify({"message": "Booking failed"}), 400
