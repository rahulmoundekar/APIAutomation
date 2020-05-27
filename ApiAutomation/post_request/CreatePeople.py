import json

import requests

file = open("user.json", 'r')
data = file.read()
requests_json = json.loads(data)

response = requests.post("https://reqres.in/api/users", requests_json)
print(response.content)
assert response.status_code == 201

print(response.headers.get("Content-Type"))