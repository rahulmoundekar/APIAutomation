import json

import requests

response = requests.delete("https://reqres.in/api/users/7")
print(response.status_code)

assert response.status_code == 204
