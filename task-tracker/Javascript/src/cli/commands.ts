import { Command } from "commander";
import {
    addTask,
    changeStatus,
    deleteTask,
    listTasks,
    updateTask,
} from "../services/taskServices.js";
import type { Status } from "../types/Task.js";

export const registerCommands = (program: Command) => {
    // Add a new Task
    program
        .command("add <description>")
        .description("Add a new task")
        .action(async (description: string) => {
            const task = await addTask(description);
            console.log(`Task added successfully! (ID: ${task.id})`);
        });

    // Update Existing Task
    program
        .command("update <id> <description>")
        .description("Update the description of existing task")
        .action(async (id: string, description: string) => {
            const updatedTask = await updateTask(id, description);
            if (!updatedTask) {
                console.log(`Task with ID ${id} not found`);
                return;
            }
            console.log(`Task updated successfully (ID: ${id})`);
        });

    // Mark a task as In Progress
    program
        .command("mark-in-progress <id>")
        .description("Mark a task as In Progress")
        .action(async (id: string) => {
            const updatedTask = await changeStatus(id, "In Progress");
            if (!updatedTask) {
                console.log(`Task with ID ${id} not found`);
                return;
            }
            console.log(`Task marked as In Progress (ID: ${id})`);
        });

    // Mark a task as Done
    program
        .command("mark-done <id>")
        .description("Mark a task as Done")
        .action(async (id: string) => {
            const updatedTask = await changeStatus(id, "Done");
            if (!updatedTask) {
                console.log(`Task with ID ${id} not found`);
                return;
            }
            console.log(`Task marked as Done (ID: ${id})`);
        });

    // Delete a task
    program
        .command("delete <id>")
        .description("Delete a task")
        .action(async (id: string) => {
            const status = await deleteTask(id);
            if (status) {
                console.log(`Task with ID ${id} deleted.`);
            } else {
                console.log(`Task with ID ${id} not found`);
                return;
            }
        });

    // List tasks (Optionally with status)
    program
        .command("list")
        .description("List tasks, optionally filtered by status")
        .argument("[status]", "filter by status (todo, in-progress, done)")
        .action(async (status?: string) => {
            let filter: string[] = [];
            if (status) {
                const normalized = status.toLowerCase();

                const statusMap: Record<string, Status> = {
                    todo: "Todo",
                    "in-progress": "In Progress",
                    done: "Done",
                };

                if (!statusMap[normalized]) {
                    console.log(`Invalid status: ${status}`);
                    return;
                }

                filter = [statusMap[normalized]];
            }

            const tasks = await listTasks(filter);

            if (tasks.length === 0) {
                console.log("No tasks found.");
                return;
            }

            tasks.forEach((t) => {
                console.log(
                    `[${t.status}] (ID: ${t.id}) ${t.description} — updated at ${t.updated_at}`,
                );
            });
        });
};
