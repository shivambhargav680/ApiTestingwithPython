import requests
import json
import jsonpath


#API URL
url = "https://reqres.in/api/users?page=2"

# Read input json file

file = open("C:\\Users\\admin\\Documents\\Post_request.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

#print(request_json)

response = requests.post(url,request_json)
#print(response.content)

# Validating status code
assert response.status_code == 201

# Fetch Header from response
print(response.headers.get("Content-Length"))

# Parse response to json format
response_json = json.loads(response.text)

# Pick id using json data
id = jsonpath.jsonpath(response_json,'id')
print(id[0])