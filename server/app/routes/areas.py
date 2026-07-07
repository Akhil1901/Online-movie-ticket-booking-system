from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.area_service import AreaService
from app.schemas.area_schema import AreaSchema

areas_bp = Blueprint(
    "areas",
    __name__,
    url_prefix="/api/areas"
)


# =====================================
# Create Area
# =====================================
@areas_bp.route("", methods=["POST"])
@jwt_required()
def create_area():

    data = request.get_json()

    success, result = AreaService.create(data)

    if success:
        return AreaSchema.success(
            "Area Created Successfully",
            result
        ), 201

    return AreaSchema.error(
        "Area Creation Failed",
        result
    ), 400


# =====================================
# Get All Areas
# =====================================
@areas_bp.route("", methods=["GET"])
def get_all_areas():

    areas = AreaService.get_all()

    return AreaSchema.success(
        "Areas Retrieved Successfully",
        areas
    ), 200


# =====================================
# Get Area By ID
# =====================================
@areas_bp.route("/<int:area_id>", methods=["GET"])
def get_area(area_id):

    area = AreaService.get_by_id(area_id)

    if not area:
        return AreaSchema.error(
            "Area Not Found"
        ), 404

    return AreaSchema.success(
        "Area Retrieved Successfully",
        area
    ), 200


# =====================================
# Update Area
# =====================================
@areas_bp.route("/<int:area_id>", methods=["PUT"])
@jwt_required()
def update_area(area_id):

    data = request.get_json()

    success, result = AreaService.update(
        area_id,
        data
    )

    if success:
        return AreaSchema.success(
            "Area Updated Successfully",
            result
        )

    return AreaSchema.error(
        "Update Failed",
        result
    ), 404


# =====================================
# Delete Area
# =====================================
@areas_bp.route("/<int:area_id>", methods=["DELETE"])
@jwt_required()
def delete_area(area_id):

    success, result = AreaService.delete(area_id)

    if success:
        return AreaSchema.success(
            "Area Deleted Successfully",
            result
        )

    return AreaSchema.error(
        "Delete Failed",
        result
    ), 404