from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='templates')

SCORE = {"player": 0, "IA": 0}


def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
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
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name


def play(player_choice):
    player_number = name_to_number(player_choice)
    player_choice = number_to_name(player_number)
    print("Player chooses %s" % (player_choice))

    # generate computer choice
    computer_choice = random.randrange(4)
    comp_number = number_to_name(computer_choice)
    print("IA chooses %s" % (comp_number))

    # using modulo to determine the winner
    result = (player_number - computer_choice) % 5

    if result >= 3 and result <= 4:
        print("IA wins!")
        SCORE["IA"] += 1
        print("score:" + str(SCORE))
        print()

    elif result >= 1 and result <= 2:
        print("Player wins!")
        SCORE["player"] += 1
        print("score:" + str(SCORE))
        print()

    else:
        print("It's a Tie!")
        print()


@app.route('/', methods=['GET', 'POST'])
def game():
    #player_input = request.form['player_input']
    #game.play_a_game(player_input)
    name = "Player"
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']

    return render_template('index.html', name=name)


@app.route('/<choice>', methods=['GET', 'POST'])
def player_input():
    choice = request.form['player_input']
    return render_template('index.html', 'play',choice)


if __name__ == '__main__':
    app.run(debug=True)

