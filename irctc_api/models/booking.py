from app import db

class Booking(db.Model):
    __tablename__ = "booking"  # ✅ Ensure correct table name

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # ✅ Corrected ForeignKey
    train_id = db.Column(db.Integer, db.ForeignKey("trains.id"), nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)

