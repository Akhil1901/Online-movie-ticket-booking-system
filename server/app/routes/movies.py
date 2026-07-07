from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.movie_service import MovieService
from app.schemas.movie_schema import MovieSchema

movies_bp = Blueprint(
    "movies",
    __name__,
    url_prefix="/api/movies"
)


# ==========================
# Create Movie
# ==========================
@movies_bp.route("", methods=["POST"])
@jwt_required()
def create_movie():

    data = request.get_json()

    success, result = MovieService.create(data)

    if success:
        return MovieSchema.success(
            "Movie Created Successfully",
            result
        ), 201

    return MovieSchema.error(
        "Movie Creation Failed",
        result
    ), 400


# ==========================
# Get All Movies
# ==========================
@movies_bp.route("", methods=["GET"])
def get_all_movies():

    movies = MovieService.get_all()

    return MovieSchema.success(
        "Movies Retrieved Successfully",
        movies
    ), 200


# ==========================
# Get Movie By ID
# ==========================
@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):

    movie = MovieService.get_by_id(movie_id)

    if not movie:
        return MovieSchema.error(
            "Movie Not Found"
        ), 404

    return MovieSchema.success(
        "Movie Retrieved Successfully",
        movie
    ), 200


# ==========================
# Update Movie
# ==========================
@movies_bp.route("/<int:movie_id>", methods=["PUT"])
@jwt_required()
def update_movie(movie_id):

    data = request.get_json()

    success, result = MovieService.update(
        movie_id,
        data
    )

    if success:
        return MovieSchema.success(
            "Movie Updated Successfully",
            result
        ), 200

    return MovieSchema.error(
        "Update Failed",
        result
    ), 404


# ==========================
# Delete Movie
# ==========================
@movies_bp.route("/<int:movie_id>", methods=["DELETE"])
@jwt_required()
def delete_movie(movie_id):

    success, result = MovieService.delete(movie_id)

    if success:
        return MovieSchema.success(
            "Movie Deleted Successfully",
            result
        ), 200

    return MovieSchema.error(
        "Delete Failed",
        result
    ), 404