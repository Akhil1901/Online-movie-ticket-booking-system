from datetime import datetime

from app.database.db import db


class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey("movies.id"),
        nullable=False
    )

    screen_id = db.Column(
        db.Integer,
        db.ForeignKey("screens.id"),
        nullable=False
    )

    show_date = db.Column(
        db.Date,
        nullable=False
    )

    start_time = db.Column(
        db.Time,
        nullable=False
    )

    end_time = db.Column(
        db.Time,
        nullable=False
    )

    ticket_price = db.Column(
        db.Float,
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

    movie = db.relationship(
        "Movie",
        backref="shows"
    )

    screen = db.relationship(
        "Screen",
        backref="shows"
    )

    def __repr__(self):
        return f"<Show {self.id}>"