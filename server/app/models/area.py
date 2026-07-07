from datetime import datetime

from app.database.db import db


class Area(db.Model):
    __tablename__ = "areas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    city_id = db.Column(
        db.Integer,
        db.ForeignKey("cities.id"),
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
    city = db.relationship(
        "City",
        backref="areas"
    )

    def __repr__(self):
        return f"<Area {self.name}>"
    