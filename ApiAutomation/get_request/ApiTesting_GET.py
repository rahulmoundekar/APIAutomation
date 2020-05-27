import json

import requests

response = requests.get("https://reqres.in/api/users?page=2")

# print(response) #<Response [200]>

print(response.content)  # its provided un formatted response content

# pretty-print json
pretty_json = json.loads(response.text)
print(json.dumps(pretty_json, indent=2))
