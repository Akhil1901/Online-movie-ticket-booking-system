from app.models.city import City
from app.repositories.city_repository import CityRepository
from app.validators.city_validator import CityValidator
from app.schemas.city_schema import CitySchema


class CityService:
    """
    City Business Logic
    """

    @staticmethod
    def create(data):

        # Validate Request
        errors = CityValidator.validate(data)

        if errors:
            return False, errors

        # Check Duplicate City
        city = CityRepository.get_by_name(data["name"])

        if city:
            return False, {
                "name": "City already exists."
            }

        # Create City Object
        city = City(
            name=data["name"],
            state=data["state"]
        )

        CityRepository.create(city)

        return True, {
            "message": "City Created Successfully",
            "city": CitySchema.city_response(city)
        }

    @staticmethod
    def get_all():

        cities = CityRepository.get_all()

        return [
            CitySchema.city_response(city)
            for city in cities
        ]

    @staticmethod
    def get_by_id(city_id):

        city = CityRepository.get_by_id(city_id)

        if not city:
            return None

        return CitySchema.city_response(city)

    @staticmethod
    def update(city_id, data):

        city = CityRepository.get_by_id(city_id)

        if not city:
            return False, {
                "city": "City not found."
            }

        city.name = data.get("name", city.name)
        city.state = data.get("state", city.state)

        CityRepository.update()

        return True, {
            "message": "City Updated Successfully",
            "city": CitySchema.city_response(city)
        }

    @staticmethod
    def delete(city_id):

        city = CityRepository.get_by_id(city_id)

        if not city:
            return False, {
                "city": "City not found."
            }

        CityRepository.delete(city)

        return True, {
            "message": "City Deleted Successfully"
        }