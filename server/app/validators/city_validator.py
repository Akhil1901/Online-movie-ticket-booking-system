class CityValidator:
    """
    City Validation Class
    """

    @staticmethod
    def validate(data):
        errors = {}

        # City Name
        if not data.get("name"):
            errors["name"] = "City name is required."

        elif len(data["name"].strip()) < 2:
            errors["name"] = "City name must be at least 2 characters."

        # State
        if not data.get("state"):
            errors["state"] = "State is required."

        elif len(data["state"].strip()) < 2:
            errors["state"] = "State name must be at least 2 characters."

        return errors