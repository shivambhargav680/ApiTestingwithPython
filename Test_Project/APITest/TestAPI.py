import requests
import json
import jsonpath


#API URL
url = "https://reqres.in/api/users?page=2"

# Send request
response = requests.get(url)

# Display response
#print(response.content)
#print(response.headers)

# Parse response to json format
json_response = json.loads(response.text)
#print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response,"total_pages")
assert pages[0] == 5

