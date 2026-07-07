from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.show_service import ShowService
from app.schemas.show_schema import ShowSchema

shows_bp = Blueprint(
    "shows",
    __name__,
    url_prefix="/api/shows"
)


# ==========================
# Create Show
# ==========================
@shows_bp.route("", methods=["POST"])
@jwt_required()
def create_show():

    data = request.get_json()

    success, result = ShowService.create(data)

    if success:
        return ShowSchema.success(
            "Show Created Successfully",
            result
        ), 201

    return ShowSchema.error(
        "Show Creation Failed",
        result
    ), 400


# ==========================
# Get All Shows
# ==========================
@shows_bp.route("", methods=["GET"])
def get_all_shows():

    shows = ShowService.get_all()

    return ShowSchema.success(
        "Shows Retrieved Successfully",
        shows
    ), 200


# ==========================
# Get Show By ID
# ==========================
@shows_bp.route("/<int:show_id>", methods=["GET"])
def get_show(show_id):

    show = ShowService.get_by_id(show_id)

    if not show:
        return ShowSchema.error(
            "Show Not Found"
        ), 404

    return ShowSchema.success(
        "Show Retrieved Successfully",
        show
    ), 200


# ==========================
# Update Show
# ==========================
@shows_bp.route("/<int:show_id>", methods=["PUT"])
@jwt_required()
def update_show(show_id):

    data = request.get_json()

    success, result = ShowService.update(
        show_id,
        data
    )

    if success:
        return ShowSchema.success(
            "Show Updated Successfully",
            result
        ), 200

    return ShowSchema.error(
        "Update Failed",
        result
    ), 404


# ==========================
# Delete Show
# ==========================
@shows_bp.route("/<int:show_id>", methods=["DELETE"])
@jwt_required()
def delete_show(show_id):

    success, result = ShowService.delete(show_id)

    if success:
        return ShowSchema.success(
            "Show Deleted Successfully",
            result
        ), 200

    return ShowSchema.error(
        "Delete Failed",
        result
    ), 404