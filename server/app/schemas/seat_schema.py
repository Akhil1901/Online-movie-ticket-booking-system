class SeatSchema:
    """
    Seat Response Schema
    """

    @staticmethod
    def seat_response(seat):
        return {
            "id": seat.id,
            "screen_id": seat.screen_id,
            "screen_name": seat.screen.name if seat.screen else None,
            "seat_number": seat.seat_number,
            "seat_type": seat.seat_type,
            "seat_status": seat.seat_status,
            "is_active": seat.is_active,
            "created_at": seat.created_at.isoformat() if seat.created_at else None,
            "updated_at": seat.updated_at.isoformat() if seat.updated_at else None
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