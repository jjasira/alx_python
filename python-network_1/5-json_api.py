#!/usr/bin/python3

"""Import the two packages that are needed"""
import requests
import sys

if __name__ == "__main__":
    """ Set the URL"""
    url = "http://0.0.0.0:5000/search_user"

    """ Set the letter parameter q"""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    """ Set the payload"""
    payload = {'q': letter}

    """ Send a POST request"""
    response = requests.post(url, data=payload)

    try:
        """ Parse the response as JSON"""
        json_response = response.json()

        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")