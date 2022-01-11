"""
File:         super.py
Author:       Sumedh Kane
Date:         9/15/2021
Section:      41
E-mail:       sumedhk1@umbc.edu
Description:  This programs takes the user's major as an input and outputs which grade is required for CMSC 201
              to count.
"""

name = str(input("What is your name?"))

type = str(input("Are you a hero or a villan? "))
if type == "villan":
    print("%s sounds pretty evil!" %(name))
else:
    saves = int(input("How many people have you saved?"))
    if saves <= 10:
        print("Go on more patrols!")
    elif saves > 10 and saves < 100:
        print("Sounds like you're making a difference!")
    else:
        print("Wow, great job saving the city!")

