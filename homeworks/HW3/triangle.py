"""
File:    triangle.py
Author:  Sumedh Kane
Date:    10/1/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  prints a triangle with height and width given by user
"""
if __name__ == '__main__':

    height = int(input("Enter an integer height for the triangle: "))

    for i in range(height,0,-1):
        for j in range(height+1):

           #print(" " + '', end='*')
            if i > j:
                print(" ", end='')
            else:
                print("*", end='')

        print()

