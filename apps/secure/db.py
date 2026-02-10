import sqlite3

try:
    from werkzeug.security import generate_password_hash
except ModuleNotFoundError as exc:
    raise RuntimeError(
        "Missing dependency 'werkzeug'. Install dependencies with: "
        "pip install -r apps/secure/requirements.txt"
    ) from exc

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
"""

SEED = [
    ("admin", generate_password_hash("admin123")),
    ("alice", generate_password_hash("alicepass"))
]


def init_db(path):
    conn = sqlite3.connect(path)
    try:
        conn.executescript(SCHEMA)
        cur = conn.cursor()
        for u, p in SEED:
            try:
                cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", (u, p))
            except sqlite3.IntegrityError:
                pass
        conn.commit()
    finally:
        conn.close()


def get_db(path):
    return sqlite3.connect(path)