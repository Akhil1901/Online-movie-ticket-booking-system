from app.models.booking import Booking
from app.repositories.booking_repository import BookingRepository
from app.repositories.user_repository import UserRepository
from app.repositories.show_repository import ShowRepository
from app.repositories.seat_repository import SeatRepository
from app.schemas.booking_schema import BookingSchema
from app.validators.booking_validator import BookingValidator


class BookingService:
    """
    Booking Business Logic
    """

    @staticmethod
    def create(data):

        errors = BookingValidator.validate(data)

        if errors:
            return False, errors

        user = UserRepository.get_by_id(data["user_id"])
        if not user:
            return False, {
                "user_id": "User not found."
            }

        show = ShowRepository.get_by_id(data["show_id"])
        if not show:
            return False, {
                "show_id": "Show not found."
            }

        seat = SeatRepository.get_by_id(data["seat_id"])
        if not seat:
            return False, {
                "seat_id": "Seat not found."
            }

        if seat.seat_status == "Booked":
            return False, {
                "seat": "Seat is already booked."
            }

        booking = Booking(
            user_id=data["user_id"],
            show_id=data["show_id"],
            seat_id=data["seat_id"],
            total_amount=data["total_amount"],
            booking_status=data.get("booking_status", "Confirmed")
        )

        BookingRepository.create(booking)

        seat.seat_status = "Booked"
        SeatRepository.update()

        return True, {
            "message": "Booking Created Successfully",
            "booking": BookingSchema.booking_response(booking)
        }

    @staticmethod
    def get_all():

        bookings = BookingRepository.get_all()

        return [
            BookingSchema.booking_response(booking)
            for booking in bookings
        ]

    @staticmethod
    def get_by_id(booking_id):

        booking = BookingRepository.get_by_id(booking_id)

        if not booking:
            return None

        return BookingSchema.booking_response(booking)

    @staticmethod
    def update(booking_id, data):

        booking = BookingRepository.get_by_id(booking_id)

        if not booking:
            return False, {
                "booking": "Booking not found."
            }

        if "booking_status" in data:
            booking.booking_status = data["booking_status"]

        if "total_amount" in data:
            booking.total_amount = data["total_amount"]

        BookingRepository.update()

        return True, {
            "message": "Booking Updated Successfully",
            "booking": BookingSchema.booking_response(booking)
        }

    @staticmethod
    def delete(booking_id):

        booking = BookingRepository.get_by_id(booking_id)

        if not booking:
            return False, {
                "booking": "Booking not found."
            }

        seat = booking.seat
        if seat:
            seat.seat_status = "Available"

        SeatRepository.update()
        BookingRepository.delete(booking)

        return True, {
            "message": "Booking Deleted Successfully"
        }