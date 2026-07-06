from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask import jsonify


def jwt_required_custom(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        try:
            verify_jwt_in_request()

        except Exception:
            return jsonify({
                "status": "error",
                "message": "Authentication Required"
            }), 401

        return fn(*args, **kwargs)

    return wrapper