from datetime import datetime

from app.database.db import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    genre = db.Column(
        db.String(100),
        nullable=False
    )

    language = db.Column(
        db.String(50),
        nullable=False
    )

    duration = db.Column(
        db.Integer,
        nullable=False
    )

    rating = db.Column(
        db.Float,
        default=0.0
    )

    release_date = db.Column(
        db.Date,
        nullable=False
    )

    poster_url = db.Column(
        db.String(500),
        nullable=True
    )

    trailer_url = db.Column(
        db.String(500),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
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

    def __repr__(self):
        return f"<Movie {self.title}>"