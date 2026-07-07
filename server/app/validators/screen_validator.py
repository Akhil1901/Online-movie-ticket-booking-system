class ScreenValidator:
    """
    Screen Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Screen Name
        if not data.get("name"):
            errors["name"] = "Screen name is required."

        elif len(data["name"].strip()) < 2:
            errors["name"] = "Screen name must be at least 2 characters."

        # Theatre ID
        if not data.get("theatre_id"):
            errors["theatre_id"] = "Theatre ID is required."

        # Total Seats
        if not data.get("total_seats"):
            errors["total_seats"] = "Total seats are required."

        else:
            try:
                seats = int(data["total_seats"])
                if seats <= 0:
                    errors["total_seats"] = "Total seats must be greater than 0."
            except (ValueError, TypeError):
                errors["total_seats"] = "Total seats must be a number."

        # Screen Type
        if not data.get("screen_type"):
            errors["screen_type"] = "Screen type is required."

        return errors