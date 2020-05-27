import json

import jsonpath
import requests

file = open("E:/OnlyForPython/SELENIUM/APIAutomation/user.json", 'r')
data = file.read()
requests_json = json.loads(data)

response = requests.put("https://reqres.in/api/users/2", requests_json)
print(response.content)

response_json = json.loads(response.text)

updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])
