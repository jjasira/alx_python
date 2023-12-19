#!/usr/bin/python3

"""we will use the folloeing two packages"""
import requests
import sys

if __name__ == "__main__":
    """we will take a url"""
    url = sys.argv[1]
    
    """Send a get request for the data that we want"""
    response = requests.get(url)
    
    x_request_id = response.headers.get('X-Request-Id')
    
    print(f"{x_request_id}")