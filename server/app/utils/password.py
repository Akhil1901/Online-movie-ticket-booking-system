from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


def hash_password(password: str) -> str:
    """
    Hash a plain text password.
    """
    return generate_password_hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against its hash.
    """
    return check_password_hash(hashed_password, password)