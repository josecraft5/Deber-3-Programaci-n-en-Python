import requests

from googletrans import Translator
traductor = Translator()
def traducir_texto(texto):
    try:
        resultado = traductor.translate(texto, src="en", dest="es")
        return resultado.text
    except:
        return texto  
# Aqui me ayudo un poco la IA para saber como traducir con src y dest igualmente me permitio entender como funciona el try y except

def peticion_random():
    url = "https://bored-api.appbrewery.com/random"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        bored_data = respuesta.json()
        return bored_data
    else: 
        print(f"Error obteniendo informacion: {respuesta.status_code}")


bored_dictinary = peticion_random()

def imprimir_diccionario(dic, clave, nombre, traducir=False):
    valor = dic.get(clave)

    if valor:
        if traducir and isinstance(valor, str):
            valor = traducir_texto(valor)

        print(f"{nombre}: {valor}")

imprimir_diccionario(bored_dictinary, "activity", "Actividad", True)
imprimir_diccionario(bored_dictinary, "type", "Tipo", True)
imprimir_diccionario(bored_dictinary, "participants", "Participantes")
imprimir_diccionario(bored_dictinary, "price", "Precio")
imprimir_diccionario(bored_dictinary, "duration", "Duracion")
imprimir_diccionario(bored_dictinary, "kidFriendly", "Amistoso con Niños")
print(bored_dictinary)
