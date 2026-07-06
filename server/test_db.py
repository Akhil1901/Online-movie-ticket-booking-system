from app import create_app
from app.database.db import db

app = create_app()

with app.app_context():
    try:
        with db.engine.connect():
            print("✅ Connected to Supabase PostgreSQL Successfully!")
    except Exception as e:
        print("❌ Database Connection Failed!")
        print(e)