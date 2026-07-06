from app.database.db import migrate


def init_migrate(app, db):
    migrate.init_app(app, db)