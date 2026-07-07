from app.models.area import Area
from app.repositories.area_repository import AreaRepository
from app.repositories.city_repository import CityRepository
from app.validators.area_validator import AreaValidator
from app.schemas.area_schema import AreaSchema


class AreaService:
    """
    Area Business Logic
    """

    @staticmethod
    def create(data):

        # Validate Request
        errors = AreaValidator.validate(data)

        if errors:
            return False, errors

        # Check City Exists
        city = CityRepository.get_by_id(data["city_id"])

        if not city:
            return False, {
                "city_id": "City not found."
            }

        # Check Duplicate Area
        area = AreaRepository.get_by_name(data["name"])

        if area:
            return False, {
                "name": "Area already exists."
            }

        # Create Area
        area = Area(
            name=data["name"],
            city_id=data["city_id"]
        )

        AreaRepository.create(area)

        return True, {
            "message": "Area Created Successfully",
            "area": AreaSchema.area_response(area)
        }

    @staticmethod
    def get_all():

        areas = AreaRepository.get_all()

        return [
            AreaSchema.area_response(area)
            for area in areas
        ]

    @staticmethod
    def get_by_id(area_id):

        area = AreaRepository.get_by_id(area_id)

        if not area:
            return None

        return AreaSchema.area_response(area)

    @staticmethod
    def update(area_id, data):

        area = AreaRepository.get_by_id(area_id)

        if not area:
            return False, {
                "area": "Area not found."
            }

        area.name = data.get("name", area.name)

        if "city_id" in data:
            city = CityRepository.get_by_id(data["city_id"])

            if not city:
                return False, {
                    "city_id": "City not found."
                }

            area.city_id = data["city_id"]

        AreaRepository.update()

        return True, {
            "message": "Area Updated Successfully",
            "area": AreaSchema.area_response(area)
        }

    @staticmethod
    def delete(area_id):

        area = AreaRepository.get_by_id(area_id)

        if not area:
            return False, {
                "area": "Area not found."
            }

        AreaRepository.delete(area)

        return True, {
            "message": "Area Deleted Successfully"
        }