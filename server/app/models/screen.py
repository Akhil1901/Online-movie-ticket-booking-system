from datetime import datetime

from app.database.db import db


class Screen(db.Model):
    __tablename__ = "screens"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    theatre_id = db.Column(
        db.Integer,
        db.ForeignKey("theatres.id"),
        nullable=False
    )

    total_seats = db.Column(
        db.Integer,
        nullable=False
    )

    screen_type = db.Column(
        db.String(50),
        nullable=False
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

    # Relationship
    theatre = db.relationship(
        "Theatre",
        backref="screens"
    )

    def __repr__(self):
        return f"<Screen {self.name}>"