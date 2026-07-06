from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Database Object
db = SQLAlchemy()

# Migration Object
migrate = Migrate()