from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.services.booking_service import BookingService
from app.schemas.booking_schema import BookingSchema

bookings_bp = Blueprint(
    "bookings",
    __name__,
    url_prefix="/api/bookings"
)


# ==========================
# Create Booking
# ==========================
@bookings_bp.route("", methods=["POST"])
@jwt_required()
def create_booking():

    data = request.get_json()

    success, result = BookingService.create(data)

    if success:
        return BookingSchema.success(
            "Booking Created Successfully",
            result
        ), 201

    return BookingSchema.error(
        "Booking Creation Failed",
        result
    ), 400


# ==========================
# Get All Bookings
# ==========================
@bookings_bp.route("", methods=["GET"])
def get_all_bookings():

    bookings = BookingService.get_all()

    return BookingSchema.success(
        "Bookings Retrieved Successfully",
        bookings
    ), 200


# ==========================
# Get Booking By ID
# ==========================
@bookings_bp.route("/<int:booking_id>", methods=["GET"])
def get_booking(booking_id):

    booking = BookingService.get_by_id(booking_id)

    if not booking:
        return BookingSchema.error(
            "Booking Not Found"
        ), 404

    return BookingSchema.success(
        "Booking Retrieved Successfully",
        booking
    ), 200


# ==========================
# Update Booking
# ==========================
@bookings_bp.route("/<int:booking_id>", methods=["PUT"])
@jwt_required()
def update_booking(booking_id):

    data = request.get_json()

    success, result = BookingService.update(
        booking_id,
        data
    )

    if success:
        return BookingSchema.success(
            "Booking Updated Successfully",
            result
        ), 200

    return BookingSchema.error(
        "Update Failed",
        result
    ), 404


# ==========================
# Delete Booking
# ==========================
@bookings_bp.route("/<int:booking_id>", methods=["DELETE"])
@jwt_required()
def delete_booking(booking_id):

    success, result = BookingService.delete(booking_id)

    if success:
        return BookingSchema.success(
            "Booking Deleted Successfully",
            result
        ), 200

    return BookingSchema.error(
        "Delete Failed",
        result
    ), 404