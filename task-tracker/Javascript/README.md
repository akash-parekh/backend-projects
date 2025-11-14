Below is a complete **README.md** suitable for Roadmap.sh submission and GitHub.
Clear, structured, and fully aligned with your TypeScript + Node.js CLI Task Tracker project.

---

# 📘 **README.md — Task Tracker CLI (Node.js + TypeScript)**

````markdown
# 📝 Task Tracker CLI (Node.js + TypeScript)

A fully type-safe, command-line Task Tracker application built using **Node.js**, **TypeScript**, and **Commander**.
This project is a solution for the **Task Tracker** challenge from [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

The CLI allows you to add, update, delete, list, and update task statuses directly from your terminal.

---

## 🚀 Features

-   Add new tasks
-   Update task descriptions
-   Delete tasks
-   Mark tasks as:
    -   `Todo`
    -   `In Progress`
    -   `Done`
-   List all tasks
-   Filter tasks by status
-   Fully type-safe (TypeScript)
-   Native ES Modules
-   Persistent storage using JSON file
-   Built with clean, extensible architecture

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/akash-parekh/task-tracker-js.git
cd task-tracker-js
```
````

### 2. Install dependencies

```bash
npm install
```

### 3. Build the project

```bash
npm run build
```

### 4. Link CLI globally (optional)

This lets you use `task-cli` from anywhere:

```bash
npm link
```

---

## ▶️ Usage

After linking, use the CLI:

```bash
task-cli <command> [...options]
```

### 📌 Add a new task

```bash
task-cli add "Buy groceries"
```

**Output:**

```
Task added successfully (ID: <uuid>)
```

### 📌 Update task description

```bash
task-cli update <id> "Buy groceries and cook dinner"
```

### 📌 Delete a task

```bash
task-cli delete <id>
```

### 📌 Mark task as In Progress

```bash
task-cli mark-in-progress <id>
```

### 📌 Mark task as Done

```bash
task-cli mark-done <id>
```

### 📌 List all tasks

```bash
task-cli list
```

### 📌 List only done tasks

```bash
task-cli list done
```

### 📌 List only tasks in progress

```bash
task-cli list in-progress
```

### 📌 List only todo tasks

```bash
task-cli list todo
```

---

## 📂 Project Structure

```
.
├── src/
│   ├── cli/
│   │   └── commands.ts
│   ├── services/
│   │   └── taskService.ts
│   ├── utils/
│   │   └── file.ts
│   ├── types/
│   │   └── Task.ts
│   └── index.ts
├── data/
│   └── tasks.json
├── dist/        # Compiled JS output
├── tsconfig.json
└── package.json
```

---

## 📍 Task Schema

Each task is stored in `data/tasks.json` with the following structure:

```json
{
    "id": "string",
    "description": "string",
    "status": "Todo | In Progress | Done",
    "created_at": "ISO timestamp",
    "updated_at": "ISO timestamp"
}
```

---

## 🧰 Technologies Used

-   **Node.js**
-   **TypeScript**
-   **Commander.js**
-   **ES Modules**
-   **crypto.randomUUID**
-   **File-based persistence (fs/promises)**

---

## 🧪 Running in development mode

```bash
npm run dev
```

Runs the CLI using `ts-node`.

---

## ⚒️ Build for production

```bash
npm run build
```

Outputs compiled JS to the `dist/` directory.

---

## 🤝 Contributing

Feel free to submit issues and pull requests.

---

## ⭐ Acknowledgments

Built for the **Backend Developer Projects** section of
👉 [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
