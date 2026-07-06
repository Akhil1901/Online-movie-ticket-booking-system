from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.city_service import CityService
from app.schemas.city_schema import CitySchema

cities_bp = Blueprint(
    "cities",
    __name__,
    url_prefix="/api/cities"
)


# =====================================
# Create City
# =====================================
@cities_bp.route("", methods=["POST"])
@jwt_required()
def create_city():

    data = request.get_json()

    success, result = CityService.create(data)

    if success:
        return CitySchema.success(
            "City Created Successfully",
            result
        ), 201

    return CitySchema.error(
        "City Creation Failed",
        result
    ), 400


# =====================================
# Get All Cities
# =====================================
@cities_bp.route("", methods=["GET"])
def get_all_cities():

    cities = CityService.get_all()

    return CitySchema.success(
        "Cities Retrieved Successfully",
        cities
    ), 200


# =====================================
# Get City By ID
# =====================================
@cities_bp.route("/<int:city_id>", methods=["GET"])
def get_city(city_id):

    city = CityService.get_by_id(city_id)

    if not city:
        return CitySchema.error(
            "City Not Found"
        ), 404

    return CitySchema.success(
        "City Retrieved Successfully",
        city
    ), 200


# =====================================
# Update City
# =====================================
@cities_bp.route("/<int:city_id>", methods=["PUT"])
@jwt_required()
def update_city(city_id):

    data = request.get_json()

    success, result = CityService.update(
        city_id,
        data
    )

    if success:
        return CitySchema.success(
            "City Updated Successfully",
            result
        )

    return CitySchema.error(
        "Update Failed",
        result
    ), 404


# =====================================
# Delete City
# =====================================
@cities_bp.route("/<int:city_id>", methods=["DELETE"])
@jwt_required()
def delete_city(city_id):

    success, result = CityService.delete(city_id)

    if success:
        return CitySchema.success(
            "City Deleted Successfully",
            result
        )

    return CitySchema.error(
        "Delete Failed",
        result
    ), 404