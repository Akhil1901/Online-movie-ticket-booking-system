from datetime import datetime

from app.database.db import db


class Theatre(db.Model):
    __tablename__ = "theatres"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    address = db.Column(
        db.String(255),
        nullable=False
    )

    area_id = db.Column(
        db.Integer,
        db.ForeignKey("areas.id"),
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
    area = db.relationship(
        "Area",
        backref="theatres"
    )

    def __repr__(self):
        return f"<Theatre {self.name}>"