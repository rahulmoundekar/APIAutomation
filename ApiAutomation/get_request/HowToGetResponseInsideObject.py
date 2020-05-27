import json
import jsonpath
import requests

response = requests.get("https://reqres.in/api/users?page=2")
pretty_json = json.loads(response.text)
# print(json.dumps(pretty_json, indent=2))

data = jsonpath.jsonpath(pretty_json, "data")  # always return list of record

for item in data:
    for people in item:
        print(people['email'])
