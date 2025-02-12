from app import db

class Train(db.Model):
    __tablename__ = "trains"  # ✅ Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    train_name = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False, default=0)  # ✅ Default value

    def __init__(self, train_name, source, destination, total_seats):
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats  # ✅ Automatically set available seats

    def __repr__(self):
        return f"<Train {self.train_name} ({self.source} → {self.destination})>"



