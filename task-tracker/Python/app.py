from pathlib import Path
import argparse
import json
from datetime import datetime

TASK_FILE = Path("tasks.json")
META_FILE = Path("meta.json")


def create_files() -> None:
    # Initialize tasks.json
    if not TASK_FILE.exists():
        TASK_FILE.write_text("[]")

    # Initialize meta.json
    if not META_FILE.exists():
        META_FILE.write_text(json.dumps({"last_id": 0}, indent=4))


def load_tasks() -> list:
    try:
        data = TASK_FILE.read_text().strip()
        return json.loads(data) if data else []
    except json.JSONDecodeError:
        return []  # Recover from corrupted file


def save_tasks(tasks: list) -> None:
    TASK_FILE.write_text(json.dumps(tasks, indent=4))
    last_id = tasks[-1]["id"] if tasks else 0
    META_FILE.write_text(json.dumps({"last_id": last_id}, indent=4))


def get_last_id() -> int:
    try:
        meta = json.loads(META_FILE.read_text())
        return meta.get("last_id", 0)
    except:
        return 0


def add_task(details) -> None:
    if not details:
        print("Error: Missing task description.")
        return

    last_id = get_last_id()
    task_id = last_id + 1

    task = {
        "id": task_id,
        "description": details[0],
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added with ID: {task_id}")


def main(command, details) -> None:
    create_files()

    commands = [
        "add", "update", "delete",
        "mark-in-progress", "mark-done", "list"
    ]

    if command not in commands:
        print("Available commands:")
        for cmd in commands:
            print(" -", cmd)
        return

    if command == "add":
        add_task(details)
    elif command == "update":
        pass
    elif command == "delete":
        pass
    elif command == "mark-in-progress":
        pass
    elif command == "mark-done":
        pass
    elif command == "list":
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("command", help="Command to execute")
    parser.add_argument("details", nargs="*", help="Additional arguments")

    args = parser.parse_args()

    main(args.command, args.details)
