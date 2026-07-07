class AreaSchema:
    """
    Area Response Schema
    """

    @staticmethod
    def area_response(area):
        return {
            "id": area.id,
            "name": area.name,
            "city_id": area.city_id,
            "city_name": area.city.name if area.city else None,
            "is_active": area.is_active,
            "created_at": area.created_at.isoformat() if area.created_at else None,
            "updated_at": area.updated_at.isoformat() if area.updated_at else None
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