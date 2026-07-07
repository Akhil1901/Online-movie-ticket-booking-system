class SeatValidator:
    """
    Seat Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Screen ID
        if not data.get("screen_id"):
            errors["screen_id"] = "Screen ID is required."

        # Seat Number
        if not data.get("seat_number"):
            errors["seat_number"] = "Seat number is required."

        # Seat Type
        valid_types = ["Regular", "Premium", "VIP"]

        if not data.get("seat_type"):
            errors["seat_type"] = "Seat type is required."

        elif data["seat_type"] not in valid_types:
            errors["seat_type"] = (
                "Seat type must be Regular, Premium or VIP."
            )

        # Seat Status
        valid_status = ["Available", "Booked", "Blocked"]

        if data.get("seat_status"):

            if data["seat_status"] not in valid_status:
                errors["seat_status"] = (
                    "Seat status must be Available, Booked or Blocked."
                )

        return errors