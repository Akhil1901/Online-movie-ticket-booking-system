from datetime import datetime

from app.models.show import Show
from app.repositories.show_repository import ShowRepository
from app.repositories.movie_repository import MovieRepository
from app.repositories.screen_repository import ScreenRepository
from app.schemas.show_schema import ShowSchema
from app.validators.show_validator import ShowValidator


class ShowService:
    """
    Show Business Logic
    """

    @staticmethod
    def create(data):

        errors = ShowValidator.validate(data)

        if errors:
            return False, errors

        movie = MovieRepository.get_by_id(data["movie_id"])
        if not movie:
            return False, {
                "movie_id": "Movie not found."
            }

        screen = ScreenRepository.get_by_id(data["screen_id"])
        if not screen:
            return False, {
                "screen_id": "Screen not found."
            }

        show = Show(
            movie_id=data["movie_id"],
            screen_id=data["screen_id"],
            show_date=datetime.strptime(
                data["show_date"],
                "%Y-%m-%d"
            ).date(),
            start_time=datetime.strptime(
                data["start_time"],
                "%H:%M"
            ).time(),
            end_time=datetime.strptime(
                data["end_time"],
                "%H:%M"
            ).time(),
            ticket_price=data["ticket_price"]
        )

        ShowRepository.create(show)

        return True, {
            "message": "Show Created Successfully",
            "show": ShowSchema.show_response(show)
        }

    @staticmethod
    def get_all():

        shows = ShowRepository.get_all()

        return [
            ShowSchema.show_response(show)
            for show in shows
        ]

    @staticmethod
    def get_by_id(show_id):

        show = ShowRepository.get_by_id(show_id)

        if not show:
            return None

        return ShowSchema.show_response(show)

    @staticmethod
    def update(show_id, data):

        show = ShowRepository.get_by_id(show_id)

        if not show:
            return False, {
                "show": "Show not found."
            }

        if "movie_id" in data:
            movie = MovieRepository.get_by_id(data["movie_id"])
            if not movie:
                return False, {
                    "movie_id": "Movie not found."
                }
            show.movie_id = data["movie_id"]

        if "screen_id" in data:
            screen = ScreenRepository.get_by_id(data["screen_id"])
            if not screen:
                return False, {
                    "screen_id": "Screen not found."
                }
            show.screen_id = data["screen_id"]

        if "show_date" in data:
            show.show_date = datetime.strptime(
                data["show_date"],
                "%Y-%m-%d"
            ).date()

        if "start_time" in data:
            show.start_time = datetime.strptime(
                data["start_time"],
                "%H:%M"
            ).time()

        if "end_time" in data:
            show.end_time = datetime.strptime(
                data["end_time"],
                "%H:%M"
            ).time()

        if "ticket_price" in data:
            show.ticket_price = data["ticket_price"]

        ShowRepository.update()

        return True, {
            "message": "Show Updated Successfully",
            "show": ShowSchema.show_response(show)
        }

    @staticmethod
    def delete(show_id):

        show = ShowRepository.get_by_id(show_id)

        if not show:
            return False, {
                "show": "Show not found."
            }

        ShowRepository.delete(show)

        return True, {
            "message": "Show Deleted Successfully"
        }