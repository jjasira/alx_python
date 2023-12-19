#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    """ Set the GitHub API endpoint for the authenticated user"""
    url = "https://api.github.com/user"

    """ Set the authentication credentials"""
    auth = (username, token)

    """Send a GET request to the GitHub API"""
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(f"{user_id}")
    else:
        print(f"Error: {response.status_code} - {response.text}")