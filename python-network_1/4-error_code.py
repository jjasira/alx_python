#!/usr/bin/python3
"""Import the same packages"""
import requests
import sys

if __name__ == "__main__":
    """Prevent the script from running automatically"""
    url = sys.argv[1]

    response = requests.get(url)

    print(response.text)
    
    if response.status_code >= 400:
        """Print out the error code if its more than 400"""
        print(f"Error code: {response.status_code}")