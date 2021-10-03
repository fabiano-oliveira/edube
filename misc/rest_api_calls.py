import requests as api


astros = api.get('http://api.open-notify.org/astros.json')
print(astros.json())