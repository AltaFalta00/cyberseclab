import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(label: str, code: str, cwd: Path) -> None:
    result = subprocess.run([sys.executable, "-c", code], cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[FAIL] {label}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        raise SystemExit(result.returncode)
    print(f"[OK] {label}")


secure_code = """
import os
os.environ['FLASK_ENV'] = 'development'
import app
c = app.app.test_client()
assert c.get('/').status_code == 200
assert c.post('/login', data={'username': 'admin', 'password': 'wrong'}).status_code == 401
r = c.post('/login', data={'username': 'admin', 'password': 'admin123'}, follow_redirects=False)
assert r.status_code == 302
assert r.headers.get('Location') == '/search'
assert c.get('/search?q=test').status_code == 200
"""

vulnerable_code = """
import app
c = app.app.test_client()
assert c.get('/').status_code == 200
payload = \"' OR '1'='1' -- \"
r = c.post('/login', data={'username': payload, 'password': 'irrelevant'}, follow_redirects=False)
assert r.status_code == 200
assert 'Login ok' in r.get_data(as_text=True)
"""

run("secure smoke", secure_code, ROOT / "apps" / "secure")
run("vulnerable smoke", vulnerable_code, ROOT / "apps" / "vulnerable")

for db_file in [ROOT / "apps" / "secure" / "secure.db", ROOT / "apps" / "vulnerable" / "vuln.db"]:
    try:
        db_file.unlink()
    except FileNotFoundError:
        pass
