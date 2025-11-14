import urllib.request
import json

def get_details(username):
    url = f"https://api.github.com/users/{username}/events"
    req = urllib.request.Request(url, headers={"User-Agent": "Python"})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        return data
