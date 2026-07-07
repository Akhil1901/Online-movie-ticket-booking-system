from datetime import datetime

from app.database.db import db


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    show_id = db.Column(
        db.Integer,
        db.ForeignKey("shows.id"),
        nullable=False
    )

    seat_id = db.Column(
        db.Integer,
        db.ForeignKey("seats.id"),
        nullable=False
    )

    booking_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    booking_status = db.Column(
        db.String(20),
        default="Confirmed"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = db.relationship("User", backref="bookings")
    show = db.relationship("Show", backref="bookings")
    seat = db.relationship("Seat", backref="bookings")

    def __repr__(self):
        return f"<Booking {self.id}>"