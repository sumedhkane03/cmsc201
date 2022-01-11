"""
File:    rock_paper.py
Author:  Sumedh Kane
Date:    10/8/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  user plays rock paper scissors with the computer
"""


if __name__ == '__main__':

    import sys
    from random import choice, seed

    if len(sys.argv) >= 2:
        seed(sys.argv[1])


    throw = ''
    while throw != 'stop':
        throw = input("Throw either rock paper scissors or stop to end: ").lower()
        the_choice = choice(['rock','paper','scissors'])
        if throw == the_choice:
            print("Both %s, there is a tie." %(throw))
        elif throw == 'rock':
            if the_choice == 'paper':
                print("Paper covers rock, you lose.")
            else:
                print("Rock crushes scissors, you win.")
        elif throw == 'paper':
            if the_choice == 'scissors':
                print("Scissors covers paper, you lose.")
            else:
                print("Paper covers rock, you win.")
        elif throw == 'scissors':
            if the_choice == 'rock':
                print("Rock crushes scissors, you lose.")
            else:
                print("Scissors cut paper, you win.")
        elif throw != "stop":
            print("You need to select rock, paper or scissors.")


    print("Thank you for playing!")