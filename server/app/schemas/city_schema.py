class CitySchema:
    """
    City Response Schema
    """

    @staticmethod
    def city_response(city):
        return {
            "id": city.id,
            "name": city.name,
            "state": city.state,
            "is_active": city.is_active,
            "created_at": city.created_at.isoformat() if city.created_at else None,
            "updated_at": city.updated_at.isoformat() if city.updated_at else None
        }

    @staticmethod
    def success(message, data=None):
        return {
            "status": "success",
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message, errors=None):
        return {
            "status": "error",
            "message": message,
            "errors": errors
        }