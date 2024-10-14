from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, test, select_pokemon_type, select_all_types, select_all_stats, select_unique_random_pokemon, select_specific_stat
import random

def question_abilities():

    # Select a random pokemon for question 1
    pokemon = select_random_pokemon()

    # Question
    question = f"¿Cuál es la habilidad de {pokemon}?"

    # Select the pokemon abilities 
    abilities = select_pokemon_abilities(pokemon)

    # Select all the abilities of pokemons
    all_abilities = select_all_abilities()

    # Select the correct answer
    correct_answer = random.choice(abilities)

    # Array quiz 1
    first_quiz = [3]

    # Creat the quiz
    first_quiz = random.sample(all_abilities, 3)
    first_quiz.append(correct_answer)    
    random.shuffle(first_quiz)

    print(f"Pokemon: {pokemon}, Correct Answer: {correct_answer}, Options: {first_quiz}")  # Debugging line


    return question, first_quiz, correct_answer

def question_types():

    # Select a random pokemon for question 2
    pokemon_2 = select_random_pokemon()

    # Question
    question = f"¿De que tipo es: {pokemon_2}?"

    # Select the type of the pokemon
    pokemon_type = select_pokemon_type(pokemon_2)

    # select all the types of pokemon
    all_types = select_all_types()

    # Select the correct answer
    correct_answer = random.choice(pokemon_type)
    # Creat a new array with the pokemon type and random pokemons types
    new_all_types = [type for type in all_types if type not in pokemon_type]

    # Array quiz 2
    second_quiz = [3]

    # Fill and shuffle the array
    second_quiz = random.sample(new_all_types, 3)
    second_quiz.append(correct_answer)
    random.shuffle(second_quiz)

    return question, second_quiz, correct_answer

def stats_question():

    # Select 4 uniques randoms pokemons for question 3
    uniques_pokemons = select_unique_random_pokemon(4)
        
    # Get the stats of the pokemons 
    pokemon_1, pokemon_2, pokemon_3, pokemon_4 = uniques_pokemons

    # Set the stat of the game
    stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    stat = random.choice(stats)

    # Select the correct answer
    correct_answerd = uniques_pokemons[0]

    # Question
    question = f"¿Que Pokemon tiene mas {stat}?"

    # Check the specific stat of the pokemon
    stat_pokemon_1 = select_specific_stat(pokemon_1, stat)
    stat_pokemon_2 = select_specific_stat(pokemon_2, stat)
    stat_pokemon_3 = select_specific_stat(pokemon_3, stat)
    stat_pokemon_4 = select_specific_stat(pokemon_4, stat)

    stats_list = [stat_pokemon_1, stat_pokemon_2, stat_pokemon_3, stat_pokemon_4]

    """
    # Recorrer los Pokémon y sus estadísticas
    for i in range(1, len(uniques_pokemons)):
        if stats_list[i] > higer_stat:
            higer_stat = stats_list[i]
            pokemon_with_higher_stat = uniques_pokemons[i]
    """

    return question, uniques_pokemons, stat 


def select_random_question():

    question_functions = {
    1: question_abilities,
    2: question_types,
    3: stats_question
    }

    random_n = random.randint(1,2)

    return question_functions[random_n]()



"""""
questions = [
    {
        'name': 'stats1',
        'question': '¿Que Pokemon tiene mas {{ stat }}?'
        },
    {
        'name': 'stats2',
        'question': '¿Cuál es la stat más alta de este Pokémon: {{ pokemon_7 }}??'
        },
    {
        'name': 'stats3',
        'question': 'Cual es la stat mas baja de este pokemon {{ pokemon_8 }}?'
        },
        ]

"""""