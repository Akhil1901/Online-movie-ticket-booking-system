from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.seat_service import SeatService
from app.schemas.seat_schema import SeatSchema

seats_bp = Blueprint(
    "seats",
    __name__,
    url_prefix="/api/seats"
)


# ==========================
# Create Seat
# ==========================
@seats_bp.route("", methods=["POST"])
@jwt_required()
def create_seat():

    data = request.get_json()

    success, result = SeatService.create(data)

    if success:
        return SeatSchema.success(
            "Seat Created Successfully",
            result
        ), 201

    return SeatSchema.error(
        "Seat Creation Failed",
        result
    ), 400


# ==========================
# Get All Seats
# ==========================
@seats_bp.route("", methods=["GET"])
def get_all_seats():

    seats = SeatService.get_all()

    return SeatSchema.success(
        "Seats Retrieved Successfully",
        seats
    ), 200


# ==========================
# Get Seat By ID
# ==========================
@seats_bp.route("/<int:seat_id>", methods=["GET"])
def get_seat(seat_id):

    seat = SeatService.get_by_id(seat_id)

    if not seat:
        return SeatSchema.error(
            "Seat Not Found"
        ), 404

    return SeatSchema.success(
        "Seat Retrieved Successfully",
        seat
    ), 200


# ==========================
# Update Seat
# ==========================
@seats_bp.route("/<int:seat_id>", methods=["PUT"])
@jwt_required()
def update_seat(seat_id):

    data = request.get_json()

    success, result = SeatService.update(
        seat_id,
        data
    )

    if success:
        return SeatSchema.success(
            "Seat Updated Successfully",
            result
        ), 200

    return SeatSchema.error(
        "Update Failed",
        result
    ), 404


# ==========================
# Delete Seat
# ==========================
@seats_bp.route("/<int:seat_id>", methods=["DELETE"])
@jwt_required()
def delete_seat(seat_id):

    success, result = SeatService.delete(seat_id)

    if success:
        return SeatSchema.success(
            "Seat Deleted Successfully",
            result
        ), 200

    return SeatSchema.error(
        "Delete Failed",
        result
    ), 404