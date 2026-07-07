from app.database.db import db
from app.models.show import Show


class ShowRepository:
    """
    Repository for Show Database Operations
    """

    @staticmethod
    def get_all():
        return Show.query.all()

    @staticmethod
    def get_by_id(show_id):
        return Show.query.get(show_id)

    @staticmethod
    def create(show):
        db.session.add(show)
        db.session.commit()
        return show

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(show):
        db.session.delete(show)
        db.session.commit()