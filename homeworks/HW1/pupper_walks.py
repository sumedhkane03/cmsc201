"""
File:    pupper_walks.py
Author:  Sumedh Kane
Date:    09/17/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
This program will calculate approximately how long you walk Pupper each year.
"""
print("What is Pupper's real name?")
name = str(input())
print(name)
print('How many times per week do you walk Pupper?')
tpw = int(input())
print(tpw)
print("How long is the walk in miles?")
length = float(input())
print(length)
print("How many minutes does it take for you to walk a mile?")
minutesPerMile = int(input())
print(minutesPerMile)

totalMiles = float(tpw) * length * 52
hoursPerMile = float(minutesPerMile) / 60
totalTime = totalMiles * hoursPerMile


finalTime = round(totalTime, 2)
finalMiles = round(totalMiles, 2)

print("Your dog's name is %s, and you have walked %s miles this year, in %s hours." %(name,finalMiles,finalTime))


