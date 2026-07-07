from datetime import datetime

from app.database.db import db


class Seat(db.Model):
    __tablename__ = "seats"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    screen_id = db.Column(
        db.Integer,
        db.ForeignKey("screens.id"),
        nullable=False
    )

    seat_number = db.Column(
        db.String(10),
        nullable=False
    )

    seat_type = db.Column(
        db.String(20),
        nullable=False,
        default="Regular"
    )

    seat_status = db.Column(
        db.String(20),
        nullable=False,
        default="Available"
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

    screen = db.relationship(
        "Screen",
        backref="seats"
    )

    def __repr__(self):
        return f"<Seat {self.seat_number}>"