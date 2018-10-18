# Flint Eller
# 10/17/18
# Simulates a game of Nim

import random


def generate_piles():
    """
    This generates a random number of stones
    :return: a random number of stones
    """
    number_stones = random.randint(1, 10)
    return number_stones


def show_piles(pile_1, pile_2):
    """
    Prints stones in each pile
    :param pile_1:
    :param pile_2:
    :return:
    """
    print("Pile 1: ", pile_1)
    print("Pile 2: ", pile_2)


def main():
    # Checks if user wants to play, loops forever until 'n'
    while True:
        user_play = input("Do you want to play  game?")
        if user_play == "n":
            break
        else:
            pile_1 = generate_piles()
            pile_2 = generate_piles()
            # Starts game with piles generated and loops until both piles are empty
            while True:
                if pile_1 == 0 and pile_2 == 0:
                    break
                show_piles(pile_1, pile_2)
                # Gets user input for which pile and how many stones
                which_pile = int(input("Which pile?"))
                num_stones = int(input("How many stones?"))
                # Subtracts correct number from correct pile
                if which_pile == 1:
                    pile_1 = pile_1 - num_stones
                else:
                    pile_2 = pile_2 - num_stones
                show_piles(pile_1, pile_2)
                # Checks if user took last stones. If they did, end game, if not, keep going
                if pile_1 == 0 and pile_2 == 0:
                    print("You win!!")
                    break
                print("Computer's turn")
                # Chooses computer's pile
                if pile_1 == 0:
                    computer_pile = 2
                elif pile_2 == 0:
                    computer_pile = 1
                else:
                    computer_pile = random.randint(1, 2)
                # Chooses computer's number
                if computer_pile == 1:
                    if pile_1 <= 3:
                        pile_1 = 0
                    else:
                        pile_1 = pile_1 - 3
                else:
                    if pile_2 <= 3:
                        pile_2 = 0
                    else:
                        pile_2 = pile_2 - 3
                # Checks if computer took last stones. If it did, end game, if not, keep going
                if pile_1 == 0 and pile_2 == 0:
                    print("You loose")
                    break


main()
