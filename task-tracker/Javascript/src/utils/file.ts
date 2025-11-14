import { promises as fs } from "fs";

import type { Task } from "../types/Task.js";

const FILE_PATH = "data/tasks.json";

export const readTasks = async (): Promise<Task[]> => {
    try {
        const raw = await fs.readFile(FILE_PATH, "utf-8");
        return JSON.parse(raw) as Task[];
    } catch {
        return [];
    }
};

export const writeTasks = async (tasks: Task[]): Promise<void> => {
    await fs.writeFile(FILE_PATH, JSON.stringify(tasks, null, 2));
};
