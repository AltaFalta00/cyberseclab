param(
  [string]$DbPath = ""
)

if ($DbPath -ne "") {
  $env:DB_PATH = $DbPath
}

python apps/vulnerable/app.py
