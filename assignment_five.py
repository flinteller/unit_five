# Flint Eller
# 10/17/18
# Simulates a game of Nim

import random


def play():
    while True:
        user_play = input("Would you like to play a game of Nim?(y/n) ")
        if user_play == "y":
            return True
        elif user_play == "n":
            return False
        else:
            print("Please enter y or n")


def generate_piles():
    number_stones = random.randint(1, 10)
    return number_stones


def show_piles(pile_1, pile_2):
    print("Pile 1: ", pile_1)
    print("Pile 2: ", pile_2)


def user_pile():
    while True:
        u_pile = int(input("Which pile? (1 or 2) "))
        if u_pile == 1:
            return True
        elif u_pile == 2:
            return False
        else:
            print("Please enter a valid number")


# def user_number():
#     while True:
#         u_number = input("How many stones? (1, 2, or 3) ")
#
#
# def user_move(u_pile, u_number):
#     if u_pile == 1:
#         pass
#
#
# def computer_pile(pile_1, pile_2):
#     if pile_1 == 0:
#         return 2
#     elif pile_2 == 0:
#         return 1
#     else:
#         comp_pile = random.randint(1, 2)
#     return comp_pile
#
#
# def computer_number(comp_pile, pile):
#     if comp_pile == 1 and pile_1 == 3:
#         return 3
#     elif comp_pile == 2 and pile_2 == 3:
#         return 3
#     else:
#         return random.randint(1, 3)
#
#
#
# def computer_move(comp_pile, comp_number):
#     comp_move = comp_pile - comp_number
#     return comp_move


def main():
    user_play = play()
    while True:
        if user_play == False:
            break
        pile_1 = generate_piles()
        pile_2 = generate_piles()
        show_piles(pile_1, pile_2)
        u_pile = user_pile()
        while True:
            if u_pile == True:
                break
        # u_number = user_number()
        # user_move(u_pile, u_number)
        # comp_pile = computer_pile()
        # comp_number = computer_number()
        # computer_move(comp_pile, comp_number)
    print("Thanks for playing, bye!")


main()
