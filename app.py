from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='templates')

SCORE = {"player": 0, "IA": 0}
IA_CHOICE = {"IA" : ""}


def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    return number


def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name


def play(player_choice):
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(4)
    computer_choice = number_to_name(comp_number)
    IA_CHOICE["IA"] = computer_choice

    # using modulo to determine the winner
    result = (player_number - comp_number) % 5

    if result >= 3 and result <= 4:
        SCORE["IA"] += 1
        return "IA wins!"

    elif result >= 1 and result <= 2:
        SCORE["player"] += 1
        return "Player wins!"

    else:
        return "It's a Tie!"


@app.route('/', methods=['GET', 'POST'])
def player_input():

    name = "Player"

    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']

    winner = ""

    choice = request.args.get('choice')
    if choice:
        winner = play(choice)

    return render_template('index.html', name=name, choice=choice, winner=winner, score=SCORE, ia=IA_CHOICE)


if __name__ == '__main__':
    app.run(debug=True)

