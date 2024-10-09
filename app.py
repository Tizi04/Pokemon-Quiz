from flask import Flask, render_template, request, redirect, url_for
from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, test, select_pokemon_type, select_all_types, select_all_stats, select_unique_random_pokemon
from helper2 import verify_json
import random

app = Flask(__name__)

@app.route('/')
def index():

    # Select a random pokemon for question 1
    pokemon = select_random_pokemon()
    # Select the pokemon abilities 
    abilities = select_pokemon_abilities(pokemon)
    # Select all the abilities of pokemons
    all_abilities = select_all_abilities()
    # Array quiz 1
    first_quiz = [3]
    # Fill and shuffle the array
    n_abilities = len(abilities) - 1
    n_random_abilities = random.randint(0,n_abilities)
    first_quiz = random.sample(all_abilities, 3)
    first_quiz.append(abilities[n_random_abilities])    
    random.shuffle(first_quiz)


    # Select a random pokemon for question 2
    pokemon_2 = select_random_pokemon()
    # Select the type of the pokemon
    pokemon_type = select_pokemon_type(pokemon_2)
    # select all the types of pokemon
    all_types = select_all_types()
    # Creat a new array with the pokemon type and random pokemons types
    new_all_types = [type for type in all_types if type not in pokemon_type]
    # Array quiz 2
    second_quiz = [3]
    # Fill an shuffle the array
    n_types = len(pokemon_type) - 1
    n_random_types = random.randint(0, n_types)
    second_quiz = random.sample(new_all_types, 3)
    second_quiz.append(pokemon_type[n_random_types])
    random.shuffle(second_quiz)

    # Select 4 uniques randoms pokemons for question 3
    uniques_pokemons = select_unique_random_pokemon(4)
    # Get the stats of the pokemons 
    pokemon_3, pokemon_4, pokemon_5, pokemon_6 = uniques_pokemons

    stats_pokemon_3 = select_all_stats(pokemon_3)
    stats_pokemon_4 = select_all_stats(pokemon_4)
    stats_pokemon_5 = select_all_stats(pokemon_5)
    stats_pokemon_6 = select_all_stats(pokemon_6)
    # Select a random stat for the question
    stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    stat = random.choice(stats)


    # Select a random pokemon for question 4
    pokemon_7 = select_random_pokemon()
    stats_pokemon_7 = select_all_stats(pokemon_7)
    random.shuffle(stats)

    # Select a random pokemon for question 5
    pokemon_8 = select_random_pokemon()
    stats_pokemon_8 = select_all_stats(pokemon_8)
    stats_2 = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    random.shuffle(stats_2)


    return render_template("index.html" ,pokemon=pokemon, habilidades=first_quiz, pokemon_2=pokemon_2, types=second_quiz, unique_pokemons=uniques_pokemons, stat=stat, pokemon_7=pokemon_7, stats_question_4=stats, pokemon_8=pokemon_8, stats_2=stats_2)
        


@app.route('/search', methods=['POST'])
def search():
    
    selected_habilidades = request.form.getlist('abilities')
    return f"You selected the following abilities: {selected_habilidades}"



@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        info = test()
        todos_los_detalles = verify_json()
        types = select_pokemon_type(pokemon)
        data = select_all_types()
        stats = select_all_stats(pokemon)
        return f"{todos_los_detalles}"
    
    return render_template('prueba.html')



if __name__ == "__main__":
    app.run(debug=True)

