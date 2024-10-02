import requests
import random

def select_pokemon(pokemon):
   
   url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

   response = requests.get(url)

   data = response.json()

   nombre = data.get('types')

   if nombre and len(nombre) > 0:
       primer_objeto = nombre[0]

       if 'generation' in primer_objeto and 'name' in primer_objeto['generation']:
           nombre_generacion = primer_objeto['generation']['name']


   return nombre
    
def select_random_pokemon():

    total_pokemons = 1025
    random_number = random.randint(1, total_pokemons)

    pokemon_names = []
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000" 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Get all the Pokemons
        for pokemon in data['results']:
            pokemon_names.append(pokemon['name'])
    else:
        print("Error al obtener datos:", response.status_code)

    # Get a random Pokemon
    pokemon = pokemon_names[random_number]
    # do not select pokemons that have "-"" in their name
    while "-" in pokemon:
        random_number = random.randint(1, total_pokemons)
        pokemon = pokemon_names[random_number]   

    return pokemon

def select_pokemon_abilities(pokemon):

    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    response_pokemon = requests.get(url_pokemon)

    if response_pokemon.status_code == 200:
        data_pokemon = response_pokemon.json()
        # Get the abilities of the Pokemon
        abilities = [ability['ability']['name'] for ability in data_pokemon['abilities']]
        return abilities
    else:
        return None    


def select_all_abilities():

    url = "https://pokeapi.co/api/v2/ability?limit=100"  # Para obtener habilidades
    all_abilities = []

    while url:  # Mientras haya más páginas
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Agregar las habilidades de la página actual
            all_abilities.extend([ability['name'] for ability in data['results']])
            
            # Avanzar a la siguiente página si existe
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


    return all_types