from app.database.db import db
from app.models.movie import Movie


class MovieRepository:
    """
    Repository for Movie Database Operations
    """

    @staticmethod
    def get_all():
        return Movie.query.all()

    @staticmethod
    def get_by_id(movie_id):
        return Movie.query.get(movie_id)

    @staticmethod
    def get_by_title(title):
        return Movie.query.filter_by(title=title).first()

    @staticmethod
    def create(movie):
        db.session.add(movie)
        db.session.commit()
        return movie

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(movie):
        db.session.delete(movie)
        db.session.commit()