Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -File -Include *.pyc,*.pyo | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -File -Include *.db | Remove-Item -Force -ErrorAction SilentlyContinue
