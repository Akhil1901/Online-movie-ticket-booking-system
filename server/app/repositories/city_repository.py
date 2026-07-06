from app.database.db import db
from app.models.city import City


class CityRepository:
    """
    Repository for City Database Operations
    """

    @staticmethod
    def get_all():
        return City.query.all()

    @staticmethod
    def get_by_id(city_id):
        return City.query.get(city_id)

    @staticmethod
    def get_by_name(name):
        return City.query.filter_by(name=name).first()

    @staticmethod
    def create(city):
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(city):
        db.session.delete(city)
        db.session.commit()