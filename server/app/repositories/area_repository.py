from app.database.db import db
from app.models.area import Area


class AreaRepository:
    """
    Repository for Area Database Operations
    """

    @staticmethod
    def get_all():
        return Area.query.all()

    @staticmethod
    def get_by_id(area_id):
        return Area.query.get(area_id)

    @staticmethod
    def get_by_name(name):
        return Area.query.filter_by(name=name).first()

    @staticmethod
    def create(area):
        db.session.add(area)
        db.session.commit()
        return area

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(area):
        db.session.delete(area)
        db.session.commit()