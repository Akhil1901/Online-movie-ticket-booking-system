class BookingSchema:
    """
    Booking Response Schema
    """

    @staticmethod
    def booking_response(booking):
        return {
            "id": booking.id,
            "user_id": booking.user_id,
            "show_id": booking.show_id,
            "seat_id": booking.seat_id,
            "movie_title": booking.show.movie.title if booking.show and booking.show.movie else None,
            "screen_name": booking.show.screen.name if booking.show and booking.show.screen else None,
            "seat_number": booking.seat.seat_number if booking.seat else None,
            "booking_date": booking.booking_date.isoformat() if booking.booking_date else None,
            "total_amount": booking.total_amount,
            "booking_status": booking.booking_status,
            "is_active": booking.is_active,
            "created_at": booking.created_at.isoformat() if booking.created_at else None,
            "updated_at": booking.updated_at.isoformat() if booking.updated_at else None
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