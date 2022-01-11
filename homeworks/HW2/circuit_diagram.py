"""
File:    circuit_diagram.py
Author:  Sumedh Kane
Date:    09/24/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program takes inputs of integers that equate to either true or false and put them through a logic gate series as
  shown in the instruction diagram, then outputs whether the circuit would output 1(true) or 0(false).
"""



print("An integer equalling 0 is false, any non-zero integer is true.")
a = int(input("Enter an integer for 'a' "))
b = int(input("Enter an integer for 'b' "))
c = int(input("Enter an integer for 'c' "))
d = int(input("Enter an integer for 'd' "))
e = int(input("Enter an integer for 'e' "))

if (a == 0):
    a = False
else:
    a = True

if (b == 0):
    b = False
else:
    b = True

if (c == 0):
    c = False
else:
    c = True

if (d == 0):
    d = False
else:
    d = True

if (e == 0):
    e = False
else:
    e = True


bc = b and c
d = not d
bcde = (bc or d or e)


answer = a and bcde

if (answer == True):
    answer = 1
else:
    answer = 0

print(answer)