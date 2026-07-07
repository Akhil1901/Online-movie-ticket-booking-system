class ScreenSchema:
    """
    Screen Response Schema
    """

    @staticmethod
    def screen_response(screen):
        return {
            "id": screen.id,
            "name": screen.name,
            "theatre_id": screen.theatre_id,
            "theatre_name": screen.theatre.name if screen.theatre else None,
            "total_seats": screen.total_seats,
            "screen_type": screen.screen_type,
            "is_active": screen.is_active,
            "created_at": screen.created_at.isoformat() if screen.created_at else None,
            "updated_at": screen.updated_at.isoformat() if screen.updated_at else None
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