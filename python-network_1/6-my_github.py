"""Uses the GitHub API to display the user id."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        user_data = response.json()

        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")

    except ValueError:
        print("None")
        