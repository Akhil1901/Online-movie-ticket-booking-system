class TheatreSchema:
    """
    Theatre Response Schema
    """

    @staticmethod
    def theatre_response(theatre):
        return {
            "id": theatre.id,
            "name": theatre.name,
            "address": theatre.address,
            "area_id": theatre.area_id,
            "area_name": theatre.area.name if theatre.area else None,
            "is_active": theatre.is_active,
            "created_at": theatre.created_at.isoformat() if theatre.created_at else None,
            "updated_at": theatre.updated_at.isoformat() if theatre.updated_at else None
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