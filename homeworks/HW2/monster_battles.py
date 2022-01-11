"""
File:    monster_battles.py
Author:  Sumedh Kane
Date:    09/24/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program takes the input of two supposed monsters' hitpoints and damages
  then calculates who would win in a turn by turn fight.
"""

monster1 = str(input("What is the name of the first monster?"))
damage1 = int(input("How much damage does the first monster do?"))
hitpoints1 = int(input("How many hitpoints does the first monster have?"))

monster2 = str(input("What is the name of the second monster?"))
damage2 = int(input("How much damage does the second monster do?"))
hitpoints2 = int(input("How many hitpoints does the second monster have?"))

hitsTilDeath1 = hitpoints1 / damage2
hitsTilDeath2 = hitpoints2 / damage1

if (hitsTilDeath1 < hitsTilDeath2):
    print("%s beats %s!" %(monster2,monster1))
elif (hitsTilDeath2 == hitsTilDeath1):
    print("%s and %s annihilated each other!" %(monster1,monster2))
else:
    print("%s beats %s!" %(monster1,monster2))

