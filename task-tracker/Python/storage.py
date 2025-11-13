from pathlib import Path
import json

TASKS_FILE = Path("tasks.json")
META_FILE = Path("meta.json")

def ensure_files_exist() -> None:
    if not TASKS_FILE.exists():
        TASKS_FILE.write_text("[]")
    if not META_FILE.exists():
        META_FILE.write_text(json.dumps({"last_id": 0}, indent=4))

def load_tasks() -> list:
    try:
        data = TASKS_FILE.read_text().strip()
        return json.loads(data) if data else []
    except json.JSONDecodeError:
        return []  # Recover from corrupted file

def save_tasks(tasks: list) -> None:
    TASKS_FILE.write_text(json.dumps(tasks, indent=4))
    last_id = tasks[-1]["id"] if tasks else 0
    META_FILE.write_text(json.dumps({"last_id": last_id}, indent=4))

def get_next_id() -> int:
    try:
        meta = json.loads(META_FILE.read_text())
        return meta.get("last_id", 0) + 1
    except:
        return 0
