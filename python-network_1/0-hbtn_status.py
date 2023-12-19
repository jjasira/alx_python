"""We will use the requests package to send HTTP requests"""
import requests

url = "https://alu-intranet.hbtn.io/status"
"""This is the URL to send HTTP requests"""

response = requests.get(url)
"""This is how we want to display our content"""
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")