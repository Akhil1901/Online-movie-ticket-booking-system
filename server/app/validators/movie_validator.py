from datetime import datetime


class MovieValidator:
    """
    Movie Validation Class
    """

    @staticmethod
    def validate(data):

        errors = {}

        # Title
        if not data.get("title"):
            errors["title"] = "Movie title is required."

        elif len(data["title"].strip()) < 2:
            errors["title"] = "Movie title must be at least 2 characters."

        # Genre
        if not data.get("genre"):
            errors["genre"] = "Genre is required."

        # Language
        if not data.get("language"):
            errors["language"] = "Language is required."

        # Duration
        if not data.get("duration"):
            errors["duration"] = "Duration is required."
        else:
            try:
                duration = int(data["duration"])
                if duration <= 0:
                    errors["duration"] = "Duration must be greater than 0."
            except (ValueError, TypeError):
                errors["duration"] = "Duration must be a number."

        # Rating
        if data.get("rating") is not None:
            try:
                rating = float(data["rating"])
                if rating < 0 or rating > 10:
                    errors["rating"] = "Rating must be between 0 and 10."
            except (ValueError, TypeError):
                errors["rating"] = "Rating must be a number."

        # Release Date
        if not data.get("release_date"):
            errors["release_date"] = "Release date is required."
        else:
            try:
                datetime.strptime(data["release_date"], "%Y-%m-%d")
            except ValueError:
                errors["release_date"] = "Release date must be YYYY-MM-DD."

        return errors