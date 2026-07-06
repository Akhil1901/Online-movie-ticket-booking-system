import re


def validate_registration(data):
    """
    Validate user registration data.
    """

    errors = {}

    # Full Name
    if not data.get("full_name"):
        errors["full_name"] = "Full Name is required."

    # Email
    email = data.get("email", "").strip()

    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not email:
        errors["email"] = "Email is required."

    elif not re.match(email_pattern, email):
        errors["email"] = "Invalid email format."

    # Phone
    phone = data.get("phone", "").strip()

    phone_pattern = r'^[6-9]\d{9}$'

    if not phone:
        errors["phone"] = "Phone number is required."

    elif not re.match(phone_pattern, phone):
        errors["phone"] = "Invalid Indian mobile number."

    # Password
    password = data.get("password", "")

    if not password:
        errors["password"] = "Password is required."

    elif len(password) < 8:
        errors["password"] = "Password must contain at least 8 characters."

    return errors


def validate_login(data):
    """
    Validate login data.
    """

    errors = {}

    if not data.get("email"):
        errors["email"] = "Email is required."

    if not data.get("password"):
        errors["password"] = "Password is required."

    return errors