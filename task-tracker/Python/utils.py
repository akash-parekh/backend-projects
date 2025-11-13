from storage import get_next_id

commands = ["add", "update", "delete","mark-in-progress", "mark-done", "list"]

def create_task_object(description) -> dict:
    from datetime import datetime
    return {
        "id": get_next_id(),
        "description": description,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
