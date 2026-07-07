from flask import Flask

from app.config.config import Config
from app.database.db import db, migrate
from app.extensions.jwt import jwt
from app.extensions.cors import init_cors

# Import Blueprints
from app.routes.auth import auth_bp
from app.routes.cities import cities_bp
from app.routes.areas import areas_bp
from app.routes.theatres import theatres_bp
from app.routes.screens import screens_bp
from app.routes.movies import movies_bp
from app.routes.shows import shows_bp


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
    from app.models.area import Area
    from app.models.theatre import Theatre
    from app.models.screen import Screen
    from app.models.movie import Movie
    from app.models.show import Show

    print("5. Initializing Flask-Migrate")
    migrate.init_app(app, db)

    print("6. Initializing JWT")
    jwt.init_app(app)

    print("7. Registering Blueprints")
    app.register_blueprint(auth_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(theatres_bp)
    app.register_blueprint(screens_bp)
    app.register_blueprint(movies_bp)
    app.register_blueprint(shows_bp)

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