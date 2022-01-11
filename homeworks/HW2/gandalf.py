"""
File:    gandalf.py
Author:  Sumedh Kane
Date:    09/24/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program is a guesing game that the reader plays and the game guessed which lord of the rings character they are by
  answering a series of yes or no questions.
"""
print("What Lord of the Rings Character are you? (answer in all lowercase, and yes or no questions as 'yes' or 'no') ")
race = str(input("Are you human, dwarf, elf, maiar, or hobbit? ").lower())

if (race == "human"):
    human1 = str(input("Are you the King of Gondor?").lower())
    if (human1 == "yes"):
        print("Hello Aragorn son of Arathorn!")
    else:
        human3 = str(input("Did you try to take the ring from Frodo?").lower())
        if (human3 == "yes"):
            print("You are Boromir.")
        else:
            print("You are Theoden, probably.")
elif (race == "elf"):
    elf1 = str(input("Were you in the matrix?").lower())
    if (elf1 == "yes"):
        print("You are Elrond.")
    else:
        print("You are Legolas.")
elif (race == "maiar"):
    maiar1 = str(input("Are you good or evil?").lower())
    if (maiar1 == "good"):
        print("You are Gandalf.")
    else:
        maiar2 = str(input("Did you forge the One Ring?").lower())
        if (maiar2 == "yes"):
            print("You are Sauron.")
        else:
            print("You are Saruman.")
elif (race == "hobbit"):
    hobbit1 = str(input("Did you carry the One Ring?").lower())
    if (hobbit1 == "yes"):
        print("You are Frodo Baggins.")
    else:
        print("You are either Merry or Pippin.")
elif (race == "dwarf"):
    print("You are Gimli son of Gloin.")
else:
    print("You are an Orc.")