import json
import jsonpath
import requests

response = requests.get("https://reqres.in/api/users?page=2")
pretty_json = json.loads(response.text)
# print(json.dumps(pretty_json, indent=2))

total = jsonpath.jsonpath(pretty_json, "total")  # always return list of record
print('"total" :', total[0])
# if you want to validate it by assert

assert total[0] == 15
