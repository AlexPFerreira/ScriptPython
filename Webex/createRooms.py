import requests

access_token = 'ZDY4MGQ1OGQtNTEyNC00Mjc4LWJlMmMtYzYyMzhkNmRiZjNlNGQ3YzUzMDktNTUz_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'# your_token_here'
url = 'https://webexapis.com/v1/rooms' # URL 

# Metodo de autenticação 
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Criação da Sala
params={'title': 'teste!'} # nome da Sala
res = requests.post(url, headers=headers, json=params) 
print(res.json()) # Print da criação da sala
