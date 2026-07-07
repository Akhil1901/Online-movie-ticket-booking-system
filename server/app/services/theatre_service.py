from app.models.theatre import Theatre
from app.repositories.theatre_repository import TheatreRepository
from app.repositories.area_repository import AreaRepository
from app.validators.theatre_validator import TheatreValidator
from app.schemas.theatre_schema import TheatreSchema


class TheatreService:
    """
    Theatre Business Logic
    """

    @staticmethod
    def create(data):

        # Validate Request
        errors = TheatreValidator.validate(data)

        if errors:
            return False, errors

        # Check Area Exists
        area = AreaRepository.get_by_id(data["area_id"])

        if not area:
            return False, {
                "area_id": "Area not found."
            }

        # Check Duplicate Theatre
        theatre = TheatreRepository.get_by_name(data["name"])

        if theatre:
            return False, {
                "name": "Theatre already exists."
            }

        # Create Theatre
        theatre = Theatre(
            name=data["name"],
            address=data["address"],
            area_id=data["area_id"]
        )

        TheatreRepository.create(theatre)

        return True, {
            "message": "Theatre Created Successfully",
            "theatre": TheatreSchema.theatre_response(theatre)
        }

    @staticmethod
    def get_all():

        theatres = TheatreRepository.get_all()

        return [
            TheatreSchema.theatre_response(theatre)
            for theatre in theatres
        ]

    @staticmethod
    def get_by_id(theatre_id):

        theatre = TheatreRepository.get_by_id(theatre_id)

        if not theatre:
            return None

        return TheatreSchema.theatre_response(theatre)

    @staticmethod
    def update(theatre_id, data):

        theatre = TheatreRepository.get_by_id(theatre_id)

        if not theatre:
            return False, {
                "theatre": "Theatre not found."
            }

        theatre.name = data.get("name", theatre.name)
        theatre.address = data.get("address", theatre.address)

        if "area_id" in data:
            area = AreaRepository.get_by_id(data["area_id"])

            if not area:
                return False, {
                    "area_id": "Area not found."
                }

            theatre.area_id = data["area_id"]

        TheatreRepository.update()

        return True, {
            "message": "Theatre Updated Successfully",
            "theatre": TheatreSchema.theatre_response(theatre)
        }

    @staticmethod
    def delete(theatre_id):

        theatre = TheatreRepository.get_by_id(theatre_id)

        if not theatre:
            return False, {
                "theatre": "Theatre not found."
            }

        TheatreRepository.delete(theatre)

        return True, {
            "message": "Theatre Deleted Successfully"
        }