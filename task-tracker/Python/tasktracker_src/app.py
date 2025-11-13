import argparse
from .tasks import (
    add_task, update_task, delete_task,
    list_tasks, mark_in_progress, mark_done
)


def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI",
        usage=(
            "task <command> [args]\n\n"
            "Commands:\n"
            "  add <description>\n"
            "  update <id> <new description>\n"
            "  delete <id> <id> ...\n"
            "  list [status]\n"
            "  mark-in-progress <id> <id>\n"
            "  mark-done <id> <id>\n"
        )
    )

    parser.add_argument("command")
    parser.add_argument("details", nargs="*")
    args = parser.parse_args()

    cmd = args.command
    data = args.details

    if cmd == "add":
        add_task(data)
    elif cmd == "update":
        update_task(data)
    elif cmd == "delete":
        delete_task(data)
    elif cmd == "list":
        list_tasks(data)
    elif cmd == "mark-in-progress":
        mark_in_progress(data)
    elif cmd == "mark-done":
        mark_done(data)
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
