import random

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


def play_a_game(player_choice):
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



#play_a_game("rock")
#play_a_game("Spock")
#play_a_game("paper")
#play_a_game("lizard")
#play_a_game("scissors")


# Rock-paper-scissors-lizard-Spock
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors

