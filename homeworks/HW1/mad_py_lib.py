"""
File:    mad_py_lib.py
Author:  Sumedh Kane
Date:    09/17/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program takes an input of words from the user and outputs a crazy sentence.
"""
print('Welcome to MadPyLib, what is your name? ')
userName = str(input())
print("Input any noun/subject word: ")
noun1 = str(input())
print("Input any adjective: ")
adjective = str(input())
print("Input any verb: ")
verb = str(input())
print("Input any noun/subject word: ")
noun2 = str(input())
print("Hello %s, we are going to have an amazing semester learning %s, it's going to be %s so don't worry if you need to %s from a %s." %(userName,noun1,adjective,verb,noun2))