export type Task = {
    id: string;
    description: string;
    status: Status;
    created_at: string;
    updated_at: string;
};

export type Status = "Todo" | "In Progress" | "Done";
