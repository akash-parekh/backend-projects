def parseApiResponse(event):
        eventType = event['type']
        if eventType == 'PushEvent':
            repo = event['repo']['name']
            ref = event['payload']['ref']
            branch = ref.replace("refs/heads/","") if ref else "unknown branch"
            return f"Pushed commits to {repo} ({branch})"
        elif eventType == 'WatchEvent':
            repo = event['repo']['name']
            return f"Starred {repo}"
        elif eventType == 'IssuesEvent':
            action = event['payload']['action']
            repo = event['repo']['name']
            return f"{action} an issue in {repo}"
        elif eventType == 'PullRequestEvent':
            repo = event['repo']['name']
            status = event['payload']['action']
            sourceRepo = event['payload']['pull_request']['head']['ref']
            targetRepo = event['payload']['pull_request']['base']['ref']
            if status == 'opened':
                return f"Created a Pull Requst from {sourceRepo} to {targetRepo} ({repo})"
            return f"Pull Request from {sourceRepo} to {targetRepo} ({repo})"
        elif eventType == 'ForkEvent':
            repo = event['payload']['forkee']
            return f"Forked {repo}"
        elif eventType == 'CreateEvent':
            repo = event['repo']['name']
            ref = event['payload']['ref']
            refType = event['payload']['ref_type']
            if refType == 'branch':
                return f"Created {refType} {ref} in {repo}"
            else:
                return f"Created {refType} {repo}"
        elif eventType == 'DeleteEvent':
            refType = event['payload']['ref_type']
            ref = event['payload']['ref']
            repo = event['repo']['name']
            return f"Deleted {refType} {ref} in {repo}"
        else:
            print("Invalid Event Type")
