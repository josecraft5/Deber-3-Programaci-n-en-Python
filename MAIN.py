import requests

from googletrans import Translator
traductor = Translator()
def traducir_texto(texto):
    try:
        resultado = traductor.translate(texto, src="en", dest="es")
        return resultado.text
    except:
        return texto  # si falla, muestra el original
# Aqui me ayudo un poco la IA para saber como traducir con src y dest

def peticion_random():
    url = "https://bored-api.appbrewery.com/random"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        bored_data = respuesta.json()
        return bored_data
    else: 
        print(f"Error obteniendo informacion: {respuesta.status_code}")


bored_dictinary = peticion_random()

if bored_dictinary:
    print(f"Actividad: {traducir_texto(bored_dictinary['activity'])}")
