import requests
import json

# API endpoint
url = "http://127.0.0.1:8079/tools/wolframalpha"

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Data
data = {
    "query": "5+6"
}

# Send the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.json())