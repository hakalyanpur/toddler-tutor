import sqlite3, os

if os.environ.get("FLY_APP_NAME"):
    DB_PATH = "/data/tutor.db"
else:
    DB_PATH = os.path.join(os.path.dirname(__file__), "db", "tutor.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT    NOT NULL,
            mode        TEXT    NOT NULL,
            question_id TEXT    NOT NULL,
            correct     INTEGER NOT NULL,
            ts          TEXT    NOT NULL
        )
    """)
    db.commit()
    db.close()

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def close_db(db):
    db.close()
