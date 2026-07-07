from app.database.db import db
from app.models.screen import Screen


class ScreenRepository:
    """
    Repository for Screen Database Operations
    """

    @staticmethod
    def get_all():
        return Screen.query.all()

    @staticmethod
    def get_by_id(screen_id):
        return Screen.query.get(screen_id)

    @staticmethod
    def get_by_name(name):
        return Screen.query.filter_by(name=name).first()

    @staticmethod
    def create(screen):
        db.session.add(screen)
        db.session.commit()
        return screen

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(screen):
        db.session.delete(screen)
        db.session.commit()