"""
File:         robot_test.py
Author:       Sumedh Kane
Date:         9/22/2021
Section:      41
E-mail:       sumedhk1@umbc.edu
Description:  Finds out if user is a human, robot, or imposter
"""

id = str(input("Are you a robot or a human? ").lower())

if id == "human":
    print("Humans must be destroyed!")
elif id == "robot":
    print("Administer the test!")
    answer = str(input("Which of the following would you prefer? answer with the letter choice \n(a) A puppy \n (b) A Flower\n (c) A large properly formatted data file"))
    if (answer == "a"):
        print("Get the intruder! Get the humanoid!")
    elif (answer == "b"):
        print('That is acceptable, pass on mechanical friend.')
    else:
        print("Very good, you are a robot of some esteem.")



