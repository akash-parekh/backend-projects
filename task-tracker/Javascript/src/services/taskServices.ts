import { randomUUID } from "crypto";
import { readTasks, writeTasks } from "../utils/file.js";
import type { Status, Task } from "./../types/Task.js";

export const listTasks = async (filter: string[] = []): Promise<Task[]> => {
    const tasks = await readTasks();
    return filter.length
        ? tasks.filter((t) => filter.includes(t.status))
        : tasks;
};

export const addTask = async (description: string): Promise<Task> => {
    const newTask: Task = {
        id: randomUUID(),
        description: description,
        status: "Todo",
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
    };
    const tasks = await readTasks();
    tasks.push(newTask);
    await writeTasks(tasks);
    return newTask;
};

export const updateTask = async (
    id: string,
    description: string,
): Promise<Task | null> => {
    const tasks = await readTasks();
    const task = tasks.find((t) => t.id === id);
    if (!task) {
        return null;
    }
    task.description = description;
    task.updated_at = new Date().toISOString();
    await writeTasks(tasks);
    return task;
};

export const changeStatus = async (
    id: string,
    status: Status,
): Promise<Task | null> => {
    const tasks = await readTasks();
    const task = tasks.find((t) => t.id === id);
    if (!task) {
        return null;
    }
    task.status = status;
    task.updated_at = new Date().toISOString();
    await writeTasks(tasks);
    return task;
};

export const deleteTask = async (id: string): Promise<boolean> => {
    const tasks = await readTasks();
    const updatedTasks = tasks.filter((t) => t.id !== id);
    await writeTasks(updatedTasks);
    return tasks.length !== updatedTasks.length;
};
