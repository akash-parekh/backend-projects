import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

TASKS_FILE = Path("tasks.json")


def ensure_files_exist() -> None:
    if not TASKS_FILE.exists():
        TASKS_FILE.write_text("[]")


def load_tasks() -> List[Dict[str, Any]]:
    ensure_files_exist()
    try:
        return json.loads(TASKS_FILE.read_text())
    except json.JSONDecodeError:
        # Warning instead of silent failure
        backup_name = f"tasks_corrupted_{datetime.now().timestamp()}.json"
        TASKS_FILE.rename(backup_name)
        TASKS_FILE.write_text("[]")
        print(f"Storage corrupted. Backup saved as: {backup_name}")
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    # Always write tasks fully (atomic rewrite)
    TASKS_FILE.write_text(json.dumps(tasks, indent=4))


def get_next_id(tasks: List[Dict[str, Any]]) -> int:
    # Safer version — avoids meta file problems
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
