import requests

access_token = 'NDllNDdkMTAtMWViNi00MjcxLWI1NmItZDEwZGU0NzM2NDFhMzg5Zjc1NjEtMDNj_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'#your_token_here'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDA5ZTdjMDAtMDRkZS0xMWVjLWFmYzYtYTFmYjg3OWZkMWMw'#your_room_id'
message = 'Teste mensagem via Python' # mensagem
url = 'https://webexapis.com/v1/messages' # URL

# Autenticação
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Parâmetro
params = {'roomId': room_id, 'markdown': message} # Parâmetro - Sala e mensagem
res = requests.post(url, headers=headers, json=params) # URL / Autenticação / Parâmetro 
print(res.json()) # Imprimir na tela 