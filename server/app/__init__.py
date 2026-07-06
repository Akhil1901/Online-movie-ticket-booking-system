from flask import Flask

from app.config.config import Config
from app.database.db import db, migrate
from app.extensions.jwt import jwt
from app.extensions.cors import init_cors

# Import Blueprints
from app.routes.auth import auth_bp
from app.routes.cities import cities_bp


def create_app():

    print("1. Creating Flask App")
    app = Flask(__name__)

    print("2. Loading Configuration")
    app.config.from_object(Config)

    print("3. Initializing CORS")
    init_cors(app)

    print("4. Initializing Database")
    db.init_app(app)

    # ===============================
    # Import Models
    # ===============================
    from app.models.user import User
    from app.models.city import City

    print("5. Initializing Flask-Migrate")
    migrate.init_app(app, db)

    print("6. Initializing JWT")
    jwt.init_app(app)

    print("7. Registering Blueprints")
    app.register_blueprint(auth_bp)
    app.register_blueprint(cities_bp)

    print("8. Registering Home Route")

    @app.route("/")
    def home():
        return {
            "status": "success",
            "message": "🎬 Online Movie Ticket Booking System API",
            "version": "1.0.0"
        }

    print("9. Flask App Created Successfully")

    return app