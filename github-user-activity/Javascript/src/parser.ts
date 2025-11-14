export const parseApiData = (event: any) => {
    const eventType = event["type"];
    switch (eventType) {
        case "PushEvent": {
            const repo = event["repo"]["name"];
            const ref = event["payload"]["ref"];
            let branch = "unknown branch";
            if (ref) {
                branch = ref.replace("refs/heads/", "");
            }
            return `Pushed commits to ${repo} (${branch})`;
        }
        case "WatchEvent": {
            const repo = event["repo"]["name"];
            return `Starred ${repo}`;
        }
        case "IssuesEvent": {
            const action = event["payload"]["action"];
            const repo = event["repo"]["name"];
            return `${action} an issue in ${repo}`;
        }
        case "PullRequestEvent": {
            const repo = event["repo"]["name"];
            const status = event["payload"]["action"];
            const sourceRepo = event["payload"]["pull_request"]["head"]["ref"];
            const targetRepo = event["payload"]["pull_request"]["base"]["ref"];
            if (status == "opened") {
                return `Created a Pull Requst from ${sourceRepo} to ${targetRepo} (${repo})`;
            }
            return `Pull Request from ${sourceRepo} to ${targetRepo} (${repo})`;
        }
        case "ForkEvent": {
            const repo = event["payload"]["forkee"];
            return `Forked ${repo}`;
        }
        case "CreateEvent": {
            const repo = event["repo"]["name"];
            const ref = event["payload"]["ref"];
            const refType = event["payload"]["ref_type"];
            if (refType == "branch") {
                return `Created ${refType} ${ref} in ${repo}`;
            }
            return `Created ${refType} ${repo}`;
        }
        case "DeleteEvent": {
            const refType = event["payload"]["ref_type"];
            const ref = event["payload"]["ref"];
            const repo = event["repo"]["name"];
            return `Deleted ${refType} ${ref} in ${repo}`;
        }
        default:
            return "Invalid Event type";
    }
};
