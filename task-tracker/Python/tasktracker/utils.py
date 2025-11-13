from datetime import datetime
from typing import Dict, Any

VALID_STATUSES = ["todo", "in-progress", "done"]  # Helps validation everywhere


def create_task_object(task_id: int, description: str) -> Dict[str, Any]:
    now = datetime.now().isoformat()
    return {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": now,
        "updated_at": now,
    }
