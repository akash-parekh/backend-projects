from datetime import datetime
from storage import load_tasks, save_tasks, get_next_id
from utils import create_task_object

def add_task(details) -> None:
    if not details:
        print("Error: Missing task description.")
        return
    for detail in details:
        if not detail.strip():
            print("Error: Task description cannot be empty.")
            return
        new_task = create_task_object(detail)
        tasks = load_tasks()
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added with ID: {new_task['id']}")

def update_task(details) -> None:
    if(len(details) < 2):
        print("Error: Missing task ID or new description.")
        return
    task_id = details[0]
    new_description = " ".join(details[1:])
    tasks = load_tasks()
    for task in tasks:
        if str(task["id"]) == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task ID {task_id} updated.")
            return

def delete_task(details) -> None:
    if not details:
        print("Error: Missing Task ID.")
        return

    tasks = load_tasks()
    existing_ids = {str(t["id"]) for t in tasks}

    # Print warnings for IDs that don't exist
    for task_id in details:
        if task_id not in existing_ids:
            print(f"Warning: Task ID {task_id} does not exist.")
    updated = [t for t in tasks if str(t["id"]) not in details]
    save_tasks(updated)

    # Print only the ones that were actually deleted
    deleted = [t for t in details if t in existing_ids]
    if deleted:
        print(f"Deleted task(s): {', '.join(deleted)}")

def list_tasks(details) -> None:
    tasks = load_tasks()

    if not details:
        filtered = tasks
    else:
        allowed = set(details)
        filtered = [t for t in tasks if t["status"] in allowed]

    if not filtered:
        print("No tasks match your filters.")
        return

    for t in filtered:
        print(f"[{t['id']}] {t['description']} - {t['status']}")

def mark_in_progress(details) -> None:
    if not details:
        print("Error: Missing Task ID.")
        return
    tasks = load_tasks()
    existing_ids = {str(t["id"]) for t in tasks}

    for task_id in details:
        if task_id not in existing_ids:
            print(f"Warning: Task ID {task_id} does not exist.")

    for t in tasks:
        if str(t["id"]) in details:
            t["status"] = 'in-progress'
            print(f"Task ID {t['id']} updated to In Progress")
    save_tasks(tasks)

def mark_done(details) -> None:
    if not details:
        print("Error: Missing Task ID.")
        return
    tasks = load_tasks()
    existing_ids = {str(t["id"]) for t in tasks}

    for task_id in details:
        if task_id not in existing_ids:
            print(f"Warning: Task ID {task_id} does not exist.")

    for t in tasks:
        if str(t["id"]) in details:
            t["status"] = 'done'
            print(f"Task ID {t['id']} updated to done")
    save_tasks(tasks)
