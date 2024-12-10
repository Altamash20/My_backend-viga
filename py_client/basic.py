import requests


endpoint = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint) # HTTP Request
print(get_response.text) # print raw text response
print(get_response.status_code)


# HTTP Request -> HTML 
# REST API HTTP Request -> JSON 
# JavaScript Object Notation ~ Python Dict
# print(get_response.json())
