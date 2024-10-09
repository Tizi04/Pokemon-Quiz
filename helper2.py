import requests
import json
import os

# Get all the pokemons
def get_all_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    response = requests.get(url)
    data = response.json()
    return data['results']

# get details of pokemons
def get_details_pokemons(pokemon_url):
    response = requests.get(pokemon_url)
    data = response.json()
    
    name = data['name']
    types = [tipo['type']['name'] for tipo in data['types']]
    abilities = [habilidad['ability']['name'] for habilidad in data['abilities']]
    height = data['height']
    weight = data['weight']

    pokemon_info = {
        'name': name,
        'types': types,
        'abilities': abilities,
        'height': height,
        'weight': weight
    }

    return pokemon_info

# get pokemon´s details and save in json
def save_pokemons_details(archivo_json='pokemons.json'):
    pokemons = get_all_pokemons()
    detalles_pokemons = []

    for pokemon in pokemons:
        detalles = get_details_pokemons(pokemon['url'])
        detalles_pokemons.append(detalles)

    # save in json 
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(detalles_pokemons, f, ensure_ascii=False, indent=4)

# get the file if the file exist 
def pokemons_json(archivo_json='pokemons.json'):
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return None

# Use the file
def verify_json():
    detalles_pokemons = pokemons_json()
    if detalles_pokemons is None:
        print("No se encontró el archivo JSON, obteniendo datos de la API...")
        save_pokemons_details()  # Guardar la primera vez
        detalles_pokemons = pokemons_json()  # Cargar desde el archivo
    else:
        print("Datos cargados desde el archivo JSON.")
    
    return detalles_pokemons


