class MovieSchema:
    """
    Movie Response Schema
    """

    @staticmethod
    def movie_response(movie):
        return {
            "id": movie.id,
            "title": movie.title,
            "genre": movie.genre,
            "language": movie.language,
            "duration": movie.duration,
            "rating": movie.rating,
            "release_date": movie.release_date.isoformat() if movie.release_date else None,
            "poster_url": movie.poster_url,
            "trailer_url": movie.trailer_url,
            "description": movie.description,
            "is_active": movie.is_active,
            "created_at": movie.created_at.isoformat() if movie.created_at else None,
            "updated_at": movie.updated_at.isoformat() if movie.updated_at else None
        }

    @staticmethod
    def success(message, data=None):
        return {
            "status": "success",
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message, errors=None):
        return {
            "status": "error",
            "message": message,
            "errors": errors
        }