from flask import Flask, render_template, request, redirect, url_for, session
from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, test, select_pokemon_type, select_all_types, select_all_stats, select_unique_random_pokemon
from questions import select_random_question
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
question, first_quiz, correct_answer = None, None, None


@app.route('/', methods=['GET'])
def index(): 
            
    question, first_quiz, correct_answer = select_random_question()
    session['correct_answer'] = correct_answer

    return render_template("index.html", question=question, quiz=first_quiz)
        
@app.route('/', methods=['POST'])
def validation():
    
    choice = request.form.get("p0")
    correct_answer = session.get('correct_answer')
        
    if 'ct' not in session:
        session['ct'] = 0


    print(f"Choice: {choice}, Correct Answer: {correct_answer}")  # Imprime las respuestas para ver si coinciden

    if choice == correct_answer:
        session['ct'] += 1
        print("Incremented ct")  # Verifica que se incrementa


    print(f"Session before redirect: {session}")  # Imprimir el estado de la sesión
        
    return redirect(url_for('results'))

        
@app.route('/results', methods=['GET'])
def results():

    count = session.get('ct', 0)

    return render_template("results.html", count=count)



@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        info = test()
        types = select_pokemon_type(pokemon)
        data = select_all_types()
        stats = select_all_stats(pokemon)
        return f"{data}"
    
    '''''
    # Select a random pokemon for question 4
    pokemon_7 = select_random_pokemon()
    stats_pokemon_7 = select_all_stats(pokemon_7)
    random.shuffle(stats)

    # Select a random pokemon for question 5
    pokemon_8 = select_random_pokemon()
    stats_pokemon_8 = select_all_stats(pokemon_8)
    stats_2 = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
    random.shuffle(stats_2)
    '''''
    
    return render_template('prueba.html')



if __name__ == "__main__":
    app.run(debug=True)

