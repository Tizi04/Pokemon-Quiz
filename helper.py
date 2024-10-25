import requests
import random

def test():
   
   url = f"https://pokeapi.co/api/v2/pokemon?limit=10000"

   response = requests.get(url)

   data = response.json()
   nombres = [] 

   for p in data['results']:
       nombre = p['name']
       nombres.append(nombre)
    
   return data
       
    
def select_random_pokemon():

    total_pokemons = 1025
    random_number = random.randint(1, total_pokemons)

    pokemon_names = []

    url = "https://pokeapi.co/api/v2/pokemon?limit=100000" 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for pokemon in data['results']:
            pokemon_names.append(pokemon['name'])
    else:
        print("Error al obtener datos:", response.status_code)

    pokemon = pokemon_names[random_number]

    while "-" in pokemon:
        random_number = random.randint(1, total_pokemons)
        pokemon = pokemon_names[random_number]   

    return pokemon

def select_unique_random_pokemon(n):
    selected_pokemons =  set()

    while len(selected_pokemons) < n:
        pokemon = select_random_pokemon()
        selected_pokemons.add(pokemon)

    return list(selected_pokemons)


def select_pokemon_abilities(pokemon):

    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response_pokemon = requests.get(url_pokemon)

    if response_pokemon.status_code == 200:
        data_pokemon = response_pokemon.json()
        abilities = [ability['ability']['name'] for ability in data_pokemon['abilities']]
        return abilities
    else:
        return None    


def select_all_abilities():

    url = "https://pokeapi.co/api/v2/ability?limit=100" 
    all_abilities = []

    while url:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            all_abilities.extend([ability['name'] for ability in data['results']])
            
            url = data.get('next')
        else:
            print(f"Error {response.status_code}: No se pudieron obtener las habilidades")
            return None

    return all_abilities
    
def select_pokemon_type(pokemon):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        types = []

        for slot in data['types']:
            type_name = slot['type']['name']
            types.append(type_name)
    else:
        return None
    
    return types    
    

def select_all_types():

    url = f"https://pokeapi.co/api/v2/type/"

    response = requests.get(url)
    
    if response.status_code == 200:

        all_types = []
        data = response.json()
        results = data.get('results')

        for slot in results:
            type = slot.get('name')
            if type != 'unknown':
                all_types.append(type)
    else:
        return None

    return all_types

def select_all_stats(pokemon):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        info = data.get('stats')
        stats = []

        for stat in info:
            stat_name = stat['stat']['name']
            stat_n = stat['base_stat']
            stat_object = {stat_name:stat_n}
            stats.append(stat_object)
    else:
        return None
    return stats

def select_specific_stat(pokemon, stat_name):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data.get('stats')
        stat_n = 0
        for stat in info:
            if stat['stat']['name'] == stat_name:
                stat_n = stat['base_stat']
    else:
        return None
    return stat_n


