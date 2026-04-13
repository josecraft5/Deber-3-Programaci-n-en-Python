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

def imprimir_diccionario(dic, clave, nombre, traducir=False,):
    valor = dic.get(clave)

    if valor:
        if traducir and isinstance(valor, str):
            valor = traducir_texto(valor)

        print(f"{nombre}: {valor}")

def mostrar_programa():
    imprimir_diccionario(bored_dictinary, "activity", "Actividad", True)
    imprimir_diccionario(bored_dictinary, "type", "Tipo", True)
    imprimir_diccionario(bored_dictinary, "participants", "Participantes")
    imprimir_diccionario(bored_dictinary, "price", "Precio")
    imprimir_diccionario(bored_dictinary, "availability", "Que tan facil es de realizar en una esacala del 0 al 1")
    imprimir_diccionario(bored_dictinary, "duration", "Duracion", True)
    imprimir_diccionario(bored_dictinary, "kidFriendly", "Amistoso con Niños")
    imprimir_diccionario(bored_dictinary, "link", "Link con informacion Util")

while True:
    print("\nBienvenido a Cosas que hacer cuando estas aburrido")
    print("==================")
    print("       Menu")
    print("===================")
    print("1. Actividad Aleatoria")
    print("2. Salir del programa")

    opcion = input("Seleccione una Opcion: ")

    # Validación (como te piden en clase)
    while opcion != "1" and opcion != "2":
        opcion = input("Error, seleccione una opcion correcta (1-2): ")

    if opcion == "1":
        mostrar_programa()

    elif opcion == "2":
        print("Saliendo del programa...")
        break
    

