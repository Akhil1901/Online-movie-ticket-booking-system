class AuthSchema:
    """
    Authentication Response Schema
    """

    @staticmethod
    def user_response(user):
        """
        Convert User model to JSON response.
        """
        return {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "is_active": user.is_active,
            "created_at": (
                user.created_at.isoformat()
                if user.created_at else None
            ),
            "updated_at": (
                user.updated_at.isoformat()
                if user.updated_at else None
            )
        }

    @staticmethod
    def success(message, data=None):
        """
        Standard Success Response
        """
        return {
            "status": "success",
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message, errors=None):
        """
        Standard Error Response
        """
        return {
            "status": "error",
            "message": message,
            "errors": errors
        }