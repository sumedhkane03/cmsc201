"""
File: hailstone.py
Author:
Date:
Section:
E-mail:
Description: This file contains python code that implements the "flight"
  of a hailstone, following the HOTPO rules (also known as the Collatz
  Conjecture), recursively
"""

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

def flight(height):
    """
    recursively calculates the path of a hailstone
    :param height: the height of the hailstone
    :return: a recursive call, which at the end returns the number
        of "steps"taken for the hailstone to reach a height of 1
    """
    steps = 0
    #print("Height of: ", int(height))
    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    if height <= 0 :
        print('Invalid height of: ',int(height))
        return 0
    else:
        print("Height of: ",(int(height)))
    # stops when it reachs height of 1 (the ground)
    if height == 1:
        return 0
    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2
    if height % 2 == 0:
        height /= 2
    else:
        height = (height * 3) + 1
    # if the current height is odd, multiply it by 3, then add 1
    steps+=1
    steps+=flight(height)
    return steps

if __name__ == "__main__":

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    start_height = int(input(msg))

    # recursive call goes here
    steps = flight(start_height)
    print("\nIt took", steps, "steps to hit the ground.")
    print("Thank you for using the Hailstone Simulator!\n")

