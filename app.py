from flask import Flask, render_template, request, redirect, url_for
from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, select_pokemon, select_pokemon_type, select_all_types
import random

app = Flask(__name__)

@app.route('/')
def index():
    pokemon = select_random_pokemon()
    habilidades = select_pokemon_abilities(pokemon)
    todas_habilidades = select_all_abilities()

    pokemon_2 = select_random_pokemon()
    pokemon_type = select_pokemon_type(pokemon_2)
    all_types = select_all_types()
    new_all_types = [type for type in all_types if type not in pokemon_type]

    primer_quiz = [3]
    second_quiz = [3]

    n_habilidades = len(habilidades) - 1
    n_random_habilidades = random.randint(0,n_habilidades)

    n_types = len(pokemon_type) - 1
    n_random_types = random.randint(0, n_types)
    

    primer_quiz = random.sample(todas_habilidades, 3)
    primer_quiz.append(habilidades[n_random_habilidades])    
    random.shuffle(primer_quiz)

    second_quiz = random.sample(new_all_types, 3)
    second_quiz.append(pokemon_type[n_random_types])
    random.shuffle(second_quiz)


    return render_template("index.html", pokemon=pokemon, habilidades=primer_quiz, pokemon_2=pokemon_2, types=second_quiz)
        


@app.route('/search', methods=['POST'])
def search():
    
    selected_habilidades = request.form.getlist('abilities')
    return f"You selected the following abilities: {selected_habilidades}"



@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        info = select_pokemon(pokemon)
        types = select_pokemon_type(pokemon)
        data = select_all_types()
        return f"La info de {pokemon} es: {data}"
    
    return render_template('prueba.html')



if __name__ == "__main__":
    app.run(debug=True)

