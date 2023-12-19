#!/usr/bin/python3
"""we will use the following two modules"""
import requests
import sys

if __name__ == "__main__":
    """This prevents the script from runnning automatically after being imported"""
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)