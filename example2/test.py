import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "basic-api")
# response = requests.get(BASE + "basic-api")
print(response.json())