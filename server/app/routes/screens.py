from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.screen_service import ScreenService
from app.schemas.screen_schema import ScreenSchema

screens_bp = Blueprint(
    "screens",
    __name__,
    url_prefix="/api/screens"
)


# ==========================
# Create Screen
# ==========================
@screens_bp.route("", methods=["POST"])
@jwt_required()
def create_screen():

    data = request.get_json()

    success, result = ScreenService.create(data)

    if success:
        return ScreenSchema.success(
            "Screen Created Successfully",
            result
        ), 201

    return ScreenSchema.error(
        "Screen Creation Failed",
        result
    ), 400


# ==========================
# Get All Screens
# ==========================
@screens_bp.route("", methods=["GET"])
def get_all_screens():

    screens = ScreenService.get_all()

    return ScreenSchema.success(
        "Screens Retrieved Successfully",
        screens
    ), 200


# ==========================
# Get Screen By ID
# ==========================
@screens_bp.route("/<int:screen_id>", methods=["GET"])
def get_screen(screen_id):

    screen = ScreenService.get_by_id(screen_id)

    if not screen:
        return ScreenSchema.error(
            "Screen Not Found"
        ), 404

    return ScreenSchema.success(
        "Screen Retrieved Successfully",
        screen
    ), 200


# ==========================
# Update Screen
# ==========================
@screens_bp.route("/<int:screen_id>", methods=["PUT"])
@jwt_required()
def update_screen(screen_id):

    data = request.get_json()

    success, result = ScreenService.update(
        screen_id,
        data
    )

    if success:
        return ScreenSchema.success(
            "Screen Updated Successfully",
            result
        )

    return ScreenSchema.error(
        "Update Failed",
        result
    ), 404


# ==========================
# Delete Screen
# ==========================
@screens_bp.route("/<int:screen_id>", methods=["DELETE"])
@jwt_required()
def delete_screen(screen_id):

    success, result = ScreenService.delete(screen_id)

    if success:
        return ScreenSchema.success(
            "Screen Deleted Successfully",
            result
        )

    return ScreenSchema.error(
        "Delete Failed",
        result
    ), 404