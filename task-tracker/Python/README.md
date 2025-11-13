# **TASK TRACKER**

## **Overview**

Build a command-line application to manage tasks and maintain a simple to-do system.
The application should accept commands via positional arguments, store tasks in a JSON file, and support basic task operations.

This project reinforces skills in filesystem operations, parsing CLI inputs, working with JSON, and designing a basic command-line tool.

[Link to Project](https://roadmap.sh/projects/task-tracker)

---

## **Core Features**

Your CLI should allow the user to:

-   Add new tasks
-   Update task descriptions
-   Delete tasks
-   Mark tasks as:

    -   **in progress**
    -   **done**

-   List:

    -   all tasks
    -   done tasks
    -   in-progress tasks
    -   not-done (todo) tasks

---

## **Constraints**

-   You may use **any programming language**.
-   Use **positional CLI arguments** for commands and inputs.
-   Store data in a **JSON file located in the current directory**.
-   Automatically create the JSON file if it doesn’t exist.
-   Use the **language’s native filesystem module** (no external libs).
-   Handle errors and invalid inputs gracefully.
-   No external frameworks or libraries.

---

## **Example Commands**

```bash
# Add a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Update an existing task
task-cli update 1 "Buy groceries and cook dinner"

# Delete a task
task-cli delete 1

# Mark a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# List all tasks
task-cli list

# List tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## **Task Structure**

Each task stored in the JSON file must include:

| Property      | Description                              |
| ------------- | ---------------------------------------- |
| `id`          | Unique identifier (integer)              |
| `description` | Text describing the task                 |
| `status`      | One of: `todo`, `in-progress`, `done`    |
| `createdAt`   | Timestamp when the task was created      |
| `updatedAt`   | Timestamp when the task was last updated |

Be sure to update timestamps appropriately on any modification.

---

## **Development Steps**

### **1. Setup**

-   Pick a language (e.g., Python, JavaScript).
-   Create your project folder.
-   Initialize Git for version control.

### **2. Project Initialization**

-   Set up basic file structure.
-   Prepare a simple entry point for your CLI.

### **3. Feature Implementation**

Recommended order:

1. Handle CLI argument parsing.
2. Add task creation and JSON persistence.
3. Implement listing.
4. Add updating.
5. Add status changes (in-progress, done).
6. Add deletion.
7. Add filtering by status.

### **4. Testing**

-   Test each command individually.
-   Inspect the JSON file to verify correct structure and updates.
-   Ensure proper handling of:

    -   missing IDs
    -   corrupted/empty JSON
    -   invalid commands

### **5. Finalizing**

-   Clean and organize code.
-   Add comments where helpful.
-   Write a clear README describing usage.

## **Project Structure**

    taskcli/
    │
    ├── main.py              # CLI entry point
    ├── storage.py           # load/save tasks, meta handling
    ├── tasks.py             # business logic (add, update, delete)
    └── utils.py             # helper functions (optional)
