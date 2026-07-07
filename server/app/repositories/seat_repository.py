from app.database.db import db
from app.models.seat import Seat


class SeatRepository:
    """
    Repository for Seat Database Operations
    """

    @staticmethod
    def get_all():
        return Seat.query.all()

    @staticmethod
    def get_by_id(seat_id):
        return Seat.query.get(seat_id)

    @staticmethod
    def get_by_screen(screen_id):
        return Seat.query.filter_by(screen_id=screen_id).all()

    @staticmethod
    def get_by_screen_and_number(screen_id, seat_number):
        return Seat.query.filter_by(
            screen_id=screen_id,
            seat_number=seat_number
        ).first()

    @staticmethod
    def create(seat):
        db.session.add(seat)
        db.session.commit()
        return seat

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(seat):
        db.session.delete(seat)
        db.session.commit()