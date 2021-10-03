import requests

access_token = 'NDllNDdkMTAtMWViNi00MjcxLWI1NmItZDEwZGU0NzM2NDFhMzg5Zjc1NjEtMDNj_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'#'your_token_here'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDA5ZTdjMDAtMDRkZS0xMWVjLWFmYzYtYTFmYjg3OWZkMWMw'#'your_room_id'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id) # URL + Room_id

# Authorization
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Parâmetro 
res = requests.get(url, headers=headers) # URL + Authorization
print(res.json()) # Print on screen 