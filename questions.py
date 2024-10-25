from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, test, select_pokemon_type, select_all_types, select_all_stats, select_unique_random_pokemon, select_specific_stat
import random

def question_abilities():

    pokemon = select_random_pokemon()
    abilities = select_pokemon_abilities(pokemon)
    all_abilities = select_all_abilities()

    question = f"Cuál es la habilidad de {pokemon}?"
    correct_answer = random.choice(abilities)

    first_quiz = [3]
    first_quiz = random.sample(all_abilities, 3)
    first_quiz.append(correct_answer)    
    random.shuffle(first_quiz)

    for i in range(len(first_quiz)):
        if "-" in first_quiz[i]:
            first_quiz[i] = first_quiz[i].replace("-", " ")

    print(f"Pokemon: {pokemon}, Correct Answer: {correct_answer}, Options: {first_quiz}")  # Debugging line


    return question, first_quiz, correct_answer

def question_types():


    pokemon_2 = select_random_pokemon()
    pokemon_type = select_pokemon_type(pokemon_2)
    all_types = select_all_types()

    question = f"De que tipo es {pokemon_2}?"
    correct_answer = random.choice(pokemon_type)

    new_all_types = [type for type in all_types if type not in pokemon_type]

    second_quiz = [3]
    second_quiz = random.sample(new_all_types, 3)
    second_quiz.append(correct_answer)
    random.shuffle(second_quiz)

    return question, second_quiz, correct_answer

def stats_question():

    uniques_pokemons = select_unique_random_pokemon(4)
    pokemon_1, pokemon_2, pokemon_3, pokemon_4 = uniques_pokemons
    stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    stat = random.choice(stats)

    question = f"Que Pokemon tiene mas {stat}?"

    stat_pokemon_1 = select_specific_stat(pokemon_1, stat)
    stat_pokemon_2 = select_specific_stat(pokemon_2, stat)
    stat_pokemon_3 = select_specific_stat(pokemon_3, stat)
    stat_pokemon_4 = select_specific_stat(pokemon_4, stat)

    stats_list = [stat_pokemon_1, stat_pokemon_2, stat_pokemon_3, stat_pokemon_4]
    higer_stat = 0

    for i in range(1, len(uniques_pokemons)):
        if stats_list[i] > higer_stat:
            higer_stat = stats_list[i]
            pokemon_with_higher_stat = uniques_pokemons[i]
    
    correct_answer = pokemon_with_higher_stat

    return question, uniques_pokemons, correct_answer 


def higher_pokemon_stat():


    pokemon = select_random_pokemon() 
    pokemon_stats = select_all_stats(pokemon)
    higher_stat = 0
    higher_stat_name = None
    stats_name_list = []

    question = f"Cuál es la stat más alta de {pokemon}?"

    for o in pokemon_stats:
        for k, v in o.items():
            if v > higher_stat:
                higher_stat = v
                higher_stat_name = k
            stats_name_list.append(k)

    correct_answer = higher_stat_name

    return question, stats_name_list, correct_answer


def select_random_question():
    question_functions = {
        1: question_abilities,
        2: question_types,
        3: higher_pokemon_stat,
        4: stats_question
    }

    # Seleccionar la primera pregunta
    random_n1 = random.randint(1, 4)
    first_question = question_functions[random_n1]()
    
    # Asegurarse de que la segunda pregunta sea diferente
    random_n2 = random.randint(1, 4)
    while random_n2 == random_n1:
        random_n2 = random.randint(1, 4)
    second_question = question_functions[random_n2]()
    
    # Asegurarse de que la tercera pregunta también sea diferente
    random_n3 = random.randint(1, 4)
    while random_n3 == random_n1 or random_n3 == random_n2:
        random_n3 = random.randint(1, 4)
    third_question = question_functions[random_n3]()

    return first_question, second_question, third_question


"""""
questions = [
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