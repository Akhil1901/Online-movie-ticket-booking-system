"seats_bp"
"""
Routes Package
"""

from .auth import auth_bp
from .cities import cities_bp
from .areas import areas_bp
from .theatres import theatres_bp
from .screens import screens_bp
from .movies import movies_bp
from .shows import shows_bp
from .seats import seats_bp
from .bookings import bookings_bp

__all__ = [
    "auth_bp",
    "cities_bp",
    "areas_bp",
    "theatres_bp",
    "screens_bp",
    "movies_bp",
    "shows_bp",
    "seats_bp",
    "bookings_bp"
]