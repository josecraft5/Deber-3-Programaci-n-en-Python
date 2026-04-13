import requests

base_url = "https://pokeapi.co/api/v2/"

def poke_info(nombre):
    url = f"{base_url}/pokemon/{nombre}"
    response = requests.get(url)
    # significa 200 que la conexion fue efectiva
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Fallo en obtener la informacion {response.status_code}")

pokemon_name = "rayquaza"
poke_dictionary = poke_info(pokemon_name)

if poke_dictionary:
    print(f"Nombre: {poke_dictionary['name'].capitalize()}")
    print(f"ID: {poke_dictionary['id']}")
    print(f"Peso: {poke_dictionary['weight']} kg")
    print(f"altura: {poke_dictionary['height']} m")