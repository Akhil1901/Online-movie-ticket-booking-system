from app.models.screen import Screen
from app.repositories.screen_repository import ScreenRepository
from app.repositories.theatre_repository import TheatreRepository
from app.validators.screen_validator import ScreenValidator
from app.schemas.screen_schema import ScreenSchema


class ScreenService:
    """
    Screen Business Logic
    """

    @staticmethod
    def create(data):

        # Validate Request
        errors = ScreenValidator.validate(data)

        if errors:
            return False, errors

        # Check Theatre Exists
        theatre = TheatreRepository.get_by_id(data["theatre_id"])

        if not theatre:
            return False, {
                "theatre_id": "Theatre not found."
            }

        # Check Duplicate Screen
        screen = ScreenRepository.get_by_name(data["name"])

        if screen:
            return False, {
                "name": "Screen already exists."
            }

        # Create Screen
        screen = Screen(
            name=data["name"],
            theatre_id=data["theatre_id"],
            total_seats=data["total_seats"],
            screen_type=data["screen_type"]
        )

        ScreenRepository.create(screen)

        return True, {
            "message": "Screen Created Successfully",
            "screen": ScreenSchema.screen_response(screen)
        }

    @staticmethod
    def get_all():

        screens = ScreenRepository.get_all()

        return [
            ScreenSchema.screen_response(screen)
            for screen in screens
        ]

    @staticmethod
    def get_by_id(screen_id):

        screen = ScreenRepository.get_by_id(screen_id)

        if not screen:
            return None

        return ScreenSchema.screen_response(screen)

    @staticmethod
    def update(screen_id, data):

        screen = ScreenRepository.get_by_id(screen_id)

        if not screen:
            return False, {
                "screen": "Screen not found."
            }

        screen.name = data.get("name", screen.name)
        screen.total_seats = data.get("total_seats", screen.total_seats)
        screen.screen_type = data.get("screen_type", screen.screen_type)

        if "theatre_id" in data:
            theatre = TheatreRepository.get_by_id(data["theatre_id"])

            if not theatre:
                return False, {
                    "theatre_id": "Theatre not found."
                }

            screen.theatre_id = data["theatre_id"]

        ScreenRepository.update()

        return True, {
            "message": "Screen Updated Successfully",
            "screen": ScreenSchema.screen_response(screen)
        }

    @staticmethod
    def delete(screen_id):

        screen = ScreenRepository.get_by_id(screen_id)

        if not screen:
            return False, {
                "screen": "Screen not found."
            }

        ScreenRepository.delete(screen)

        return True, {
            "message": "Screen Deleted Successfully"
        }