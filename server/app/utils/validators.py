import re


def is_valid_email(email):
    """
    Validate Email
    """

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    """
    Validate Indian Mobile Number
    """

    pattern = r'^[6-9]\d{9}$'

    return re.match(pattern, phone) is not None