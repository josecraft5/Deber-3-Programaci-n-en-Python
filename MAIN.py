import requests

url = "https://bored-api.appbrewery.com/random"

respuesta = requests.get(url)

print(respuesta.json())