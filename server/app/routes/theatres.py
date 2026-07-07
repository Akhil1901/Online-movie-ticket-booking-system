from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.theatre_service import TheatreService
from app.schemas.theatre_schema import TheatreSchema

theatres_bp = Blueprint(
    "theatres",
    __name__,
    url_prefix="/api/theatres"
)


# =====================================
# Create Theatre
# =====================================
@theatres_bp.route("", methods=["POST"])
@jwt_required()
def create_theatre():

    data = request.get_json()

    success, result = TheatreService.create(data)

    if success:
        return TheatreSchema.success(
            "Theatre Created Successfully",
            result
        ), 201

    return TheatreSchema.error(
        "Theatre Creation Failed",
        result
    ), 400


# =====================================
# Get All Theatres
# =====================================
@theatres_bp.route("", methods=["GET"])
def get_all_theatres():

    theatres = TheatreService.get_all()

    return TheatreSchema.success(
        "Theatres Retrieved Successfully",
        theatres
    ), 200


# =====================================
# Get Theatre By ID
# =====================================
@theatres_bp.route("/<int:theatre_id>", methods=["GET"])
def get_theatre(theatre_id):

    theatre = TheatreService.get_by_id(theatre_id)

    if not theatre:
        return TheatreSchema.error(
            "Theatre Not Found"
        ), 404

    return TheatreSchema.success(
        "Theatre Retrieved Successfully",
        theatre
    ), 200


# =====================================
# Update Theatre
# =====================================
@theatres_bp.route("/<int:theatre_id>", methods=["PUT"])
@jwt_required()
def update_theatre(theatre_id):

    data = request.get_json()

    success, result = TheatreService.update(
        theatre_id,
        data
    )

    if success:
        return TheatreSchema.success(
            "Theatre Updated Successfully",
            result
        )

    return TheatreSchema.error(
        "Update Failed",
        result
    ), 404


# =====================================
# Delete Theatre
# =====================================
@theatres_bp.route("/<int:theatre_id>", methods=["DELETE"])
@jwt_required()
def delete_theatre(theatre_id):

    success, result = TheatreService.delete(theatre_id)

    if success:
        return TheatreSchema.success(
            "Theatre Deleted Successfully",
            result
        )

    return TheatreSchema.error(
        "Delete Failed",
        result
    ), 404