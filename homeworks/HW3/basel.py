"""
File:    basel.py
Author:  Sumedh Kane
Date:    10/1/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  finds Euler's sum up til a certain user inputted limit.
"""
if __name__ == '__main__':
    
    n = int(input("Enter an integer greater than or equal to 1: "))
    sum = 0
    for i in range(n) :
        sum= sum + (1/((i+1)**2))
    print("Your sum is: ", sum)
