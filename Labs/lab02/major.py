"""
File:         major.py
Author:       Sumedh Kane
Date:         9/15/2021
Section:      41
E-mail:       sumedhk1@umbc.edu
Description:  This programs takes the user's major as an input and outputs which grade is required for CMSC 201
              to count.
"""
major = str(input("Please enter your major in abbreviated form in all caps: "))

if major == "CMSC" or major == "CMPE":
    print("You need to earn at least a B for CMSC 201 to count.")
else:
    print("You need to earn at least a C for CMSC 201 to count.")

