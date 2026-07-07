class BookingValidator:
    """
    Booking Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # User ID
        if not data.get("user_id"):
            errors["user_id"] = "User ID is required."

        # Show ID
        if not data.get("show_id"):
            errors["show_id"] = "Show ID is required."

        # Seat ID
        if not data.get("seat_id"):
            errors["seat_id"] = "Seat ID is required."

        # Total Amount
        if not data.get("total_amount"):
            errors["total_amount"] = "Total amount is required."
        else:
            try:
                amount = float(data["total_amount"])
                if amount <= 0:
                    errors["total_amount"] = "Total amount must be greater than 0."
            except (ValueError, TypeError):
                errors["total_amount"] = "Total amount must be a valid number."

        # Booking Status (Optional)
        valid_status = ["Confirmed", "Pending", "Cancelled"]

        if data.get("booking_status"):
            if data["booking_status"] not in valid_status:
                errors["booking_status"] = (
                    "Booking status must be Confirmed, Pending or Cancelled."
                )

        return errors