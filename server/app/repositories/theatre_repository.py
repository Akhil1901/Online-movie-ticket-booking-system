from app.database.db import db
from app.models.theatre import Theatre


class TheatreRepository:
    """
    Repository for Theatre Database Operations
    """

    @staticmethod
    def get_all():
        return Theatre.query.all()

    @staticmethod
    def get_by_id(theatre_id):
        return Theatre.query.get(theatre_id)

    @staticmethod
    def get_by_name(name):
        return Theatre.query.filter_by(name=name).first()

    @staticmethod
    def create(theatre):
        db.session.add(theatre)
        db.session.commit()
        return theatre

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(theatre):
        db.session.delete(theatre)
        db.session.commit()