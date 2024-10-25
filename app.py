from flask import Flask, render_template, request, redirect, url_for, session, flash
from helper import select_random_pokemon, select_pokemon_abilities, select_all_abilities, test, select_pokemon_type, select_all_types, select_all_stats, select_unique_random_pokemon, random_move
from questions import select_random_question
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
results_list = []

def answers():
    results_list.clear()

    selected_question, selected_question_2, selected_question_3 = select_random_question()
    ct = 0
  
    print(selected_question, selected_question_2, selected_question_3)

  
    for question in (selected_question, selected_question_2, selected_question_3):
        question_text, quiz, correct_answer = question
        results_list.append((question_text, quiz, correct_answer, ct))  
        ct += 1


@app.route('/', methods=['GET'])
def index(): 
    
    answers()
    print(results_list) 
    return render_template("index.html", results=results_list)
        
@app.route('/', methods=['POST'])
def validation():

    choices = []
    for i in range(3):
        choice = request.form.get(f"{results_list[i][3]}")  
        choices.append(choice)
        
    if any(choice is None or choice.strip() == "" for choice in choices):
        flash("Por favor selecciona una respuesta para cada pregunta.")
        return redirect(url_for('index'))  # Redirige a la página de inicio para volver a intentarlo

    session.pop('correct', None)
    session.pop('wrong', None)
    session.pop('mistakes', None)
    session.pop('successes', None)

    if 'correct' not in session:
        session['correct'] = 0

    if 'wrong' not in session:
        session['wrong'] = 0

    if 'mistakes' not in session:
        session['mistakes'] = []

    if 'successes' not in session:
        session['successes'] = []

    for i, q in enumerate(results_list):  
        correct_answer = q[2] 

        print(f"Choice: {choices[i]}, Correct Answer: {correct_answer}")  

        if choices[i] == correct_answer:  
            session['correct'] += 1
            session['successes'].append({
                'question': q[0],
                'chosen_answer': choices[i]
            })  
            print("Incremented correct")  
        else:
            session['wrong'] += 1
            session['mistakes'].append({
                'question': q[0],  
                'chosen_answer': choices[i],  
                'correct_answer': correct_answer  
            })
            print("Incremented wrong")      

    print(f"Session before redirect: {session}")  
        
    return redirect(url_for('results'))

        
@app.route('/results', methods=['GET'])
def results():

    correct = session.get('correct', 0)
    wrong = session.get('wrong', 0)
    mistakes = session.get('mistakes', [])
    succeses = session.get('successes', [])

    return render_template("results.html", correct=correct, wrong=wrong, succeses=succeses, mistakes=mistakes)



@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        info = test()
        types = select_pokemon_type(pokemon)
        data = select_all_types()
        stats = select_all_stats(pokemon)
        move = random_move()
        return f"{move}"
    
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

