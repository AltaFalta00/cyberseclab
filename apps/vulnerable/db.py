import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
"""

SEED = [
    ("admin", "admin123"),
    ("alice", "alicepass")
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
