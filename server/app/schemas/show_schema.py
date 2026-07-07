class ShowSchema:
    """
    Show Response Schema
    """

    @staticmethod
    def show_response(show):
        return {
            "id": show.id,
            "movie_id": show.movie_id,
            "movie_title": show.movie.title if show.movie else None,
            "screen_id": show.screen_id,
            "screen_name": show.screen.name if show.screen else None,
            "show_date": show.show_date.isoformat() if show.show_date else None,
            "start_time": show.start_time.strftime("%H:%M") if show.start_time else None,
            "end_time": show.end_time.strftime("%H:%M") if show.end_time else None,
            "ticket_price": show.ticket_price,
            "is_active": show.is_active,
            "created_at": show.created_at.isoformat() if show.created_at else None,
            "updated_at": show.updated_at.isoformat() if show.updated_at else None
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