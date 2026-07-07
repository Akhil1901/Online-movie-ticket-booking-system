class AreaValidator:
    """
    Area Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Area Name
        if not data.get("name"):
            errors["name"] = "Area name is required."

        elif len(data["name"].strip()) < 2:
            errors["name"] = "Area name must be at least 2 characters."

        # City ID
        if not data.get("city_id"):
            errors["city_id"] = "City ID is required."

        return errors