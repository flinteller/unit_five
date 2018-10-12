import random


def play():
    while True:
        user_play = input("Would you like to play a game pf Nim?(y/n) ")
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
    u_pile = input("Which pile? (1 or 2)")
    return u_pile


def user_number():
    u_number = input("How many stones? (1, 2, or 3)")
    return u_number


def user_move():


def main():
    while True:
        if play() == False:
            break
        pile_1 = generate_piles()
        pile_2 = generate_piles()
        show_piles(pile_1, pile_2)
        u_pile = user_pile()
        u_number = user_number()
        user_move(u_pile, u_number)
        computer_pile()
        computer_number()
    print("Thanks for playing, bye!")


main()
