import os
import re
import subprocess
import sys
from flask import Flask, request, render_template, session, redirect, url_for
from werkzeug.security import check_password_hash
from db import init_db, get_db


def load_secret_key():
    env = os.environ.get("FLASK_ENV", "production").lower()
    secret = os.environ.get("FLASK_SECRET_KEY")
    if secret:
        return secret

    if env in ("development", "dev"):
        return "dev-unsafe-local-only"

    raise RuntimeError(
        "FLASK_SECRET_KEY is required outside local development. "
        "Set it to a long random value before running this app."
    )


def resolve_db_path():
    env_db_path = os.environ.get("DB_PATH")
    if env_db_path:
        return env_db_path

    if os.path.isdir("/data"):
        return "/data/secure.db"

    return os.path.join(os.path.dirname(__file__), "secure.db")


app = Flask(__name__)
app.config["DB_PATH"] = resolve_db_path()
app.config["DB_INITIALIZED"] = False
app.config["SECRET_KEY"] = load_secret_key()
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = os.environ.get("FLASK_ENV", "production").lower() not in ("development", "dev")

ALLOWED_DIAG_TARGET = re.compile(r"^[A-Za-z0-9.\-]{1,64}$")


@app.before_request
def setup_db():
    if not app.config["DB_INITIALIZED"]:
        init_db(app.config["DB_PATH"])
        app.config["DB_INITIALIZED"] = True


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # Parameterized query (lookup hash by username)
    conn = get_db(app.config["DB_PATH"])
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
    finally:
        conn.close()

    if not row or not check_password_hash(row[2], password):
        return "Login failed", 401

    session.clear()
    session["user"] = row[1]
    return redirect(url_for("search"))


@app.route("/search")
def search():
    q = request.args.get("q", "")
    user = session.get("user", "guest")
    return render_template("search.html", q=q, user=user)


@app.route("/diag", methods=["GET", "POST"])
def diag():
    user = session.get("user", "guest")
    target = ""
    output = ""
    error = ""

    if request.method == "POST":
        target = request.form.get("target", "")
        if not ALLOWED_DIAG_TARGET.fullmatch(target):
            error = "Invalid target. Use letters, digits, dot and hyphen only."
        else:
            # No shell interpolation; input is passed as a plain argument.
            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    "import sys; print('checking ' + sys.argv[1])",
                    target,
                ],
                shell=False,
                text=True,
                capture_output=True,
            )
            output = (result.stdout or "").strip()

    return render_template("diag.html", user=user, target=target, output=output, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
