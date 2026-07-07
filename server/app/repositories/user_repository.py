from app.database.db import db
from app.models.user import User


class UserRepository:
    """
    Repository class for User database operations.
    """

    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_phone(phone):
        return User.query.filter_by(phone=phone).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user():
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()