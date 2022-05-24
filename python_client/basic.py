import requests

endpoint = "http://127.0.0.1:8000/api/api_home"

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "this is a query"})
print(get_response.text)
print(get_response.json())
print(get_response.status_code)
