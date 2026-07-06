from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.password import hash_password, verify_password
from app.validators.auth_validator import (
    validate_registration,
    validate_login
)


class AuthService:
    """
    Authentication Business Logic
    """

    @staticmethod
    def register(data):
        """
        Register a new user.
        """

        # Validate Input
        errors = validate_registration(data)

        if errors:
            return False, errors

        # Check Email
        if UserRepository.get_user_by_email(data["email"]):
            return False, {
                "email": "Email already exists."
            }

        # Check Phone
        if UserRepository.get_user_by_phone(data["phone"]):
            return False, {
                "phone": "Phone number already exists."
            }

        # Create User
        user = User(
            full_name=data["full_name"],
            email=data["email"],
            phone=data["phone"],
            password=hash_password(data["password"]),
            role="customer"
        )

        UserRepository.create_user(user)

        return True, {
            "message": "Registration Successful",
            "user": user.to_dict()
        }

    @staticmethod
    def login(data):
        """
        User Login
        """

        errors = validate_login(data)

        if errors:
            return False, errors

        user = UserRepository.get_user_by_email(data["email"])

        if not user:
            return False, {
                "email": "Invalid Email or Password."
            }

        if not verify_password(
            data["password"],
            user.password
        ):
            return False, {
                "password": "Invalid Email or Password."
            }

        return True, {
            "message": "Login Successful",
            "user": user.to_dict()
        }