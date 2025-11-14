import argparse

from .api import get_details
from .parser import parseApiResponse

def getUserInput():
    parser = argparse.ArgumentParser(
        description="Github User Activity",
        usage=(
            "github-user <username> \n\n"
        )
    )

    parser.add_argument("username")
    username = parser.parse_args().username
    data = get_details(username)
    for event in data:
        reponse = parseApiResponse(event)
        print(reponse)
