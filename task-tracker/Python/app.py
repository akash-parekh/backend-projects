import argparse
from storage import ensure_files_exist
from tasks import add_task, update_task, delete_task, list_tasks, mark_in_progress, mark_done
from utils import commands

def main() -> None:
    ensure_files_exist()

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("details", nargs="*", help="Additional arguments")
    args = parser.parse_args()
    command = args.command
    details = args.details

    if command == "add":
        add_task(details)
    elif command == "update":
        update_task(details)
    elif command == "delete":
        delete_task(details)
    elif command == "mark-in-progress":
        mark_in_progress(details)
    elif command == "mark-done":
        mark_done(details)
    elif command == "list":
        list_tasks(details)
    else:
        print(f"Error: Unknown command '{command}'.")
        print("Available commands:")
        for cmd in commands:
            print(" -", cmd)


if __name__ == "__main__":
    main()
