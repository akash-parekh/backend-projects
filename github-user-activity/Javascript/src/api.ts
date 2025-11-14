import { parseApiData } from "./parser";

export const githubApi = async (username: string): Promise<string[]> => {
    const res = await fetch(`https://api.github.com/users/${username}/events`, {
        headers: {
            "User-Agent": "Node",
        },
    });
    if (res.ok) {
        const data = await res.json();
        const parsedEvent = data.map((t: any) => parseApiData(t));
        return parsedEvent;
    } else {
        return [];
    }
};
