from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent


def safe_unlink(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def safe_rmtree(path: Path) -> None:
    shutil.rmtree(path, ignore_errors=True)


for folder in ROOT.rglob("__pycache__"):
    if folder.is_dir():
        safe_rmtree(folder)

for file_path in ROOT.rglob("*.pyc"):
    safe_unlink(file_path)

for file_path in ROOT.rglob("*.pyo"):
    safe_unlink(file_path)

for file_path in ROOT.rglob("*.db"):
    safe_unlink(file_path)

print("Cleanup complete.")
