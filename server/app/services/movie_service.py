from datetime import datetime

from app.models.movie import Movie
from app.repositories.movie_repository import MovieRepository
from app.schemas.movie_schema import MovieSchema
from app.validators.movie_validator import MovieValidator


class MovieService:

    @staticmethod
    def create(data):

        errors = MovieValidator.validate(data)

        if errors:
            return False, errors

        movie = MovieRepository.get_by_title(data["title"])

        if movie:
            return False, {
                "title": "Movie already exists."
            }

        movie = Movie(
            title=data["title"],
            genre=data["genre"],
            language=data["language"],
            duration=data["duration"],
            rating=data.get("rating", 0),
            release_date=datetime.strptime(
                data["release_date"],
                "%Y-%m-%d"
            ).date(),
            poster_url=data.get("poster_url"),
            trailer_url=data.get("trailer_url"),
            description=data.get("description")
        )

        MovieRepository.create(movie)

        return True, {
            "message": "Movie Created Successfully",
            "movie": MovieSchema.movie_response(movie)
        }

    @staticmethod
    def get_all():

        movies = MovieRepository.get_all()

        return [
            MovieSchema.movie_response(movie)
            for movie in movies
        ]

    @staticmethod
    def get_by_id(movie_id):

        movie = MovieRepository.get_by_id(movie_id)

        if not movie:
            return None

        return MovieSchema.movie_response(movie)

    @staticmethod
    def update(movie_id, data):

        movie = MovieRepository.get_by_id(movie_id)

        if not movie:
            return False, {
                "movie": "Movie not found."
            }

        movie.title = data.get("title", movie.title)
        movie.genre = data.get("genre", movie.genre)
        movie.language = data.get("language", movie.language)
        movie.duration = data.get("duration", movie.duration)
        movie.rating = data.get("rating", movie.rating)

        if data.get("release_date"):
            movie.release_date = datetime.strptime(
                data["release_date"],
                "%Y-%m-%d"
            ).date()

        movie.poster_url = data.get(
            "poster_url",
            movie.poster_url
        )

        movie.trailer_url = data.get(
            "trailer_url",
            movie.trailer_url
        )

        movie.description = data.get(
            "description",
            movie.description
        )

        MovieRepository.update()

        return True, {
            "message": "Movie Updated Successfully",
            "movie": MovieSchema.movie_response(movie)
        }

    @staticmethod
    def delete(movie_id):

        movie = MovieRepository.get_by_id(movie_id)

        if not movie:
            return False, {
                "movie": "Movie not found."
            }

        MovieRepository.delete(movie)

        return True, {
            "message": "Movie Deleted Successfully"
        }