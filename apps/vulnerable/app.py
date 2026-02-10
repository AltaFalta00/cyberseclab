import os
import subprocess
import time
from flask import Flask, request, make_response, render_template
from db import init_db, get_db


def resolve_db_path():
    env_db_path = os.environ.get("DB_PATH")
    if env_db_path:
        return env_db_path

    if os.path.isdir("/data"):
        return "/data/vuln.db"

    return os.path.join(os.path.dirname(__file__), "vuln.db")


app = Flask(__name__)
app.config["DB_PATH"] = resolve_db_path()
app.config["DB_INITIALIZED"] = False

# Insecure, in-memory session store
SESSIONS = {}


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

    # SQLi: direct string concatenation
    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = get_db(app.config["DB_PATH"])
    cur = conn.cursor()
    try:
        cur.execute(query)
        row = cur.fetchone()
    finally:
        conn.close()

    if not row:
        return "Login failed", 401

    # Weak session token (predictable)
    token = f"{username}:{int(time.time())}"
    SESSIONS[token] = {"user": username}
    resp = make_response("Login ok. Go to /search")
    resp.set_cookie("sid", token, httponly=False, secure=False, samesite="Lax")
    return resp


@app.route("/search")
def search():
    q = request.args.get("q", "")
    sid = request.cookies.get("sid", "")
    user = SESSIONS.get(sid, {}).get("user", "guest")

    # XSS: reflect query without escaping
    return render_template("search.html", q=q, user=user)


@app.route("/diag", methods=["GET", "POST"])
def diag():
    sid = request.cookies.get("sid", "")
    user = SESSIONS.get(sid, {}).get("user", "guest")
    target = ""
    output = ""

    if request.method == "POST":
        target = request.form.get("target", "")
        # Command injection: user-controlled input in shell command.
        cmd = f"echo checking {target}"
        output = subprocess.getoutput(cmd)

    return render_template("diag.html", user=user, target=target, output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
