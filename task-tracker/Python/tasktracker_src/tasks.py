from typing import List
from datetime import datetime

from .storage import load_tasks, save_tasks, get_next_id
from .utils import create_task_object, VALID_STATUSES


def _update_timestamp(task):
    task["updated_at"] = datetime.now().isoformat()


def add_task(details: List[str]) -> None:
    if not details:
        print("Missing task description.")
        return

    tasks = load_tasks()
    task_id = get_next_id(tasks)

    new_task = create_task_object(task_id, " ".join(details))
    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added with ID: {task_id}")


def update_task(details: List[str]) -> None:
    if len(details) < 2:
        print("Usage: update <task_id> <new description>")
        return

    try:
        task_id = int(details[0])
    except ValueError:
        print("Invalid task ID.")
        return

    tasks = load_tasks()
    new_description = " ".join(details[1:])

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            _update_timestamp(task)
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return

    print(f"Task ID {task_id} not found.")


def delete_task(details: List[str]) -> None:
    if not details:
        print("Usage: delete <task_id> <task_id> ...")
        return

    try:
        ids = [int(i) for i in details]
    except ValueError:
        print("Invalid task ID(s).")
        return

    tasks = load_tasks()
    existing_ids = {t["id"] for t in tasks}

    not_found = [i for i in ids if i not in existing_ids]
    for nf in not_found:
        print(f"Task ID {nf} does not exist.")

    remaining = [t for t in tasks if t["id"] not in ids]

    save_tasks(remaining)

    deleted = [str(i) for i in ids if i in existing_ids]
    if deleted:
        print(f"Deleted task(s): {', '.join(deleted)}")


def list_tasks(filters: List[str]) -> None:
    tasks = load_tasks()

    # Validate status filters
    for f in filters:
        if f not in VALID_STATUSES:
            print(f"Invalid status filter: {f}. Allowed: {', '.join(VALID_STATUSES)}")
            return

    if filters:
        tasks = [t for t in tasks if t["status"] in filters]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


def _change_status(details: List[str], new_status: str) -> None:
    if not details:
        print(f"Usage: mark-{new_status} <task_id> <task_id> ...")
        return

    try:
        ids = [int(i) for i in details]
    except ValueError:
        print("Invalid task ID(s).")
        return

    tasks = load_tasks()
    existing_ids = {t["id"] for t in tasks}

    for task in tasks:
        if task["id"] in ids:
            task["status"] = new_status
            _update_timestamp(task)

    for i in ids:
        if i not in existing_ids:
            print(f"Task ID {i} does not exist.")

    save_tasks(tasks)
    print(f"Updated tasks to '{new_status}'.")


def mark_in_progress(details: List[str]) -> None:
    _change_status(details, "in-progress")


def mark_done(details: List[str]) -> None:
    _change_status(details, "done")
