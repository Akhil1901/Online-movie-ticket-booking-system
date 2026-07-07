from datetime import datetime


class ShowValidator:
    """
    Show Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Movie ID
        if not data.get("movie_id"):
            errors["movie_id"] = "Movie ID is required."

        # Screen ID
        if not data.get("screen_id"):
            errors["screen_id"] = "Screen ID is required."

        # Show Date
        if not data.get("show_date"):
            errors["show_date"] = "Show date is required."
        else:
            try:
                datetime.strptime(data["show_date"], "%Y-%m-%d")
            except ValueError:
                errors["show_date"] = "Show date must be YYYY-MM-DD."

        # Start Time
        if not data.get("start_time"):
            errors["start_time"] = "Start time is required."
        else:
            try:
                datetime.strptime(data["start_time"], "%H:%M")
            except ValueError:
                errors["start_time"] = "Start time must be HH:MM (24-hour format)."

        # End Time
        if not data.get("end_time"):
            errors["end_time"] = "End time is required."
        else:
            try:
                datetime.strptime(data["end_time"], "%H:%M")
            except ValueError:
                errors["end_time"] = "End time must be HH:MM (24-hour format)."

        # Ticket Price
        if not data.get("ticket_price"):
            errors["ticket_price"] = "Ticket price is required."
        else:
            try:
                price = float(data["ticket_price"])
                if price <= 0:
                    errors["ticket_price"] = "Ticket price must be greater than 0."
            except (ValueError, TypeError):
                errors["ticket_price"] = "Ticket price must be a number."

        return errors