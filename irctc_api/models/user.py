from app import db

class User(db.Model):
    __tablename__ = "users"  # ✅ Ensure this matches the ForeignKey reference

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="user")


