from app.models.seat import Seat
from app.repositories.seat_repository import SeatRepository
from app.repositories.screen_repository import ScreenRepository
from app.schemas.seat_schema import SeatSchema
from app.validators.seat_validator import SeatValidator


class SeatService:
    """
    Seat Business Logic
    """

    @staticmethod
    def create(data):

        errors = SeatValidator.validate(data)

        if errors:
            return False, errors

        screen = ScreenRepository.get_by_id(data["screen_id"])

        if not screen:
            return False, {
                "screen_id": "Screen not found."
            }

        existing = SeatRepository.get_by_screen_and_number(
            data["screen_id"],
            data["seat_number"]
        )

        if existing:
            return False, {
                "seat_number": "Seat already exists for this screen."
            }

        seat = Seat(
            screen_id=data["screen_id"],
            seat_number=data["seat_number"],
            seat_type=data["seat_type"],
            seat_status=data.get("seat_status", "Available")
        )

        SeatRepository.create(seat)

        return True, {
            "message": "Seat Created Successfully",
            "seat": SeatSchema.seat_response(seat)
        }

    @staticmethod
    def get_all():

        seats = SeatRepository.get_all()

        return [
            SeatSchema.seat_response(seat)
            for seat in seats
        ]

    @staticmethod
    def get_by_id(seat_id):

        seat = SeatRepository.get_by_id(seat_id)

        if not seat:
            return None

        return SeatSchema.seat_response(seat)

    @staticmethod
    def update(seat_id, data):

        seat = SeatRepository.get_by_id(seat_id)

        if not seat:
            return False, {
                "seat": "Seat not found."
            }

        if "seat_number" in data:
            existing = SeatRepository.get_by_screen_and_number(
                seat.screen_id,
                data["seat_number"]
            )

            if existing and existing.id != seat.id:
                return False, {
                    "seat_number": "Seat number already exists."
                }

            seat.seat_number = data["seat_number"]

        if "seat_type" in data:
            seat.seat_type = data["seat_type"]

        if "seat_status" in data:
            seat.seat_status = data["seat_status"]

        SeatRepository.update()

        return True, {
            "message": "Seat Updated Successfully",
            "seat": SeatSchema.seat_response(seat)
        }

    @staticmethod
    def delete(seat_id):

        seat = SeatRepository.get_by_id(seat_id)

        if not seat:
            return False, {
                "seat": "Seat not found."
            }

        SeatRepository.delete(seat)

        return True, {
            "message": "Seat Deleted Successfully"
        }