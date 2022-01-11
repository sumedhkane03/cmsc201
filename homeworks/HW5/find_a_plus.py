"""
File:    find_a_plus.py
Author:  Sumedh Kane
Date:    10/22/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  Takes user input of their own and the winning lottery ticket, then outputs the amount of money won.
"""
import random




def generate_grid(m, n, seed=0):
   if seed:
       random.seed(seed)
   return [[random.choice(['.', '*']) for _ in range(n)] for _ in range(m)]


def display_grid(the_grid):
   for row in the_grid:
       print(' '.join(row))


def is_plus_there(a_grid):
   tester = []
   for i in range(len(a_grid)):
      for j in range(len(a_grid[i])):
         if j-1 >= 0 and j+1 < len(a_grid[i]):

            if a_grid[i][j] == '*' and a_grid[i][j+1] == '*' and a_grid[i][j-1] == '*' and a_grid[i-1][j] == '*' and a_grid[i+1][j] == '*':
               #tester.append(True)
                return True
            #else:
               #tester.append(False)
   return False
"""
   if True in tester:
      return True
   else:
      return False
"""






if __name__ == '__main__':
   numbers = input('Enter the dimensions (and optionally the seed): ').split()
   x = int(numbers[0])
   y = int(numbers[1])
   the_seed = int(numbers[2])
   a_grid = generate_grid(x, y, the_seed)
   display_grid(a_grid)
   print(is_plus_there(a_grid) is not False)
