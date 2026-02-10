param(
  [string]$DbPath = ""
)

$env:FLASK_ENV = "development"
if ($DbPath -ne "") {
  $env:DB_PATH = $DbPath
}

python apps/secure/app.py
