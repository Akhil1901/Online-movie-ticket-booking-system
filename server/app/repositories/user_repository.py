from app.database.db import db
from app.models.user import User


class UserRepository:
    """
    Repository class for User database operations.
    """

    @staticmethod
    def create_user(user):
        """
        Save a new user to the database.
        """
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get user by ID.
        """
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_user_by_email(email):
        """
        Get user by email.
        """
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_phone(phone):
        """
        Get user by phone number.
        """
        return User.query.filter_by(phone=phone).first()

    @staticmethod
    def get_all_users():
        """
        Get all users.
        """
        return User.query.all()

    @staticmethod
    def update_user():
        """
        Commit updated user data.
        """
        db.session.commit()

    @staticmethod
    def delete_user(user):
        """
        Delete a user.
        """
        db.session.delete(user)
        db.session.commit()