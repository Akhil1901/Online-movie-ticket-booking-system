from flask import Blueprint, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from app.services.auth_service import AuthService
from app.schemas.auth_schema import AuthSchema

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


# =====================================
# Register
# =====================================
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    success, result = AuthService.register(data)

    if success:
        return AuthSchema.success(
            "User Registered Successfully",
            result
        ), 201

    return AuthSchema.error(
        "Registration Failed",
        result
    ), 400


# =====================================
# Login
# =====================================
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    success, result = AuthService.login(data)

    if not success:
        return AuthSchema.error(
            "Login Failed",
            result
        ), 401

    access_token = create_access_token(
        identity=str(result["user"]["id"])
    )

    result["access_token"] = access_token

    return AuthSchema.success(
        "Login Successful",
        result
    ), 200


# =====================================
# Profile (Protected Route)
# =====================================
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return {
        "status": "success",
        "message": "JWT Token Verified Successfully",
        "user_id": current_user
    }, 200