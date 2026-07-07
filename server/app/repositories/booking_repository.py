from app.database.db import db
from app.models.booking import Booking


class BookingRepository:
    """
    Repository for Booking Database Operations
    """

    @staticmethod
    def get_all():
        return Booking.query.all()

    @staticmethod
    def get_by_id(booking_id):
        return Booking.query.get(booking_id)

    @staticmethod
    def get_by_user(user_id):
        return Booking.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_show(show_id):
        return Booking.query.filter_by(show_id=show_id).all()

    @staticmethod
    def create(booking):
        db.session.add(booking)
        db.session.commit()
        return booking

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(booking):
        db.session.delete(booking)
        db.session.commit()