import requests
import json

access_token = 'NDllNDdkMTAtMWViNi00MjcxLWI1NmItZDEwZGU0NzM2NDFhMzg5Zjc1NjEtMDNj_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf' # your_token_here'
url = 'https://webexapis.com/v1/people' # URL 

# Authentication 
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Parameter 
params = {
    'email': 'user@example.com'
}

res = requests.get(url, headers=headers, params=params) # URL / Authentication / Parameter
print(json.dumps(res.json(), indent=4)) # Print on screen 