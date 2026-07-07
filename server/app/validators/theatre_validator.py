class TheatreValidator:
    """
    Theatre Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Theatre Name
        if not data.get("name"):
            errors["name"] = "Theatre name is required."

        elif len(data["name"].strip()) < 2:
            errors["name"] = "Theatre name must be at least 2 characters."

        # Address
        if not data.get("address"):
            errors["address"] = "Theatre address is required."

        elif len(data["address"].strip()) < 5:
            errors["address"] = "Address must be at least 5 characters."

        # Area ID
        if not data.get("area_id"):
            errors["area_id"] = "Area ID is required."

        return errors