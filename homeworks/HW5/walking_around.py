"""
File:    walking_around.py
Author:  Sumedh Kane
Date:    10/22/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  Takes a string input, finds a certain string within the string and replaces it with a specified third string.
"""
import random

"""
    This is where your constants should generally go in the future.  

    We use all caps to indicate constants (a variable whose value we aren't going to change during the program).  
"""
ALLOWED = '_'
FORBIDDEN = '*'


def walk_around(the_grid, walk_command):
    """
    :param the_grid: a 2 dimensional list of dimensions m x n
    :param walk_command: a string composed of u, d, l, r.
            u moves in the -1 direction for the first index
            d moves in the +1 direction for the first index
            l moves in the -1 direction for the second index
            r moves in the +1 direction for the second index
    :return: a list of the [row, col] position of the character after they start at [0, 0]
    """
    k = 0
    h=0
    cur_pos = the_grid
    for i in range(len(walk_command)):

        if walk_command[i].lower() == 'r' and k < len(the_grid[h]) and the_grid[h][k+1] != '*':
            #cur_pos = cur_pos[h][k+1]
            h = h
            k = k+1
        elif walk_command[i].lower() == 'd' and h < len(the_grid) and the_grid[h+1][k] != '*':
            #cur_pos = cur_pos[h+1][k]
            h+=1
        elif walk_command[i].lower() == 'l' and k > 0 and the_grid[h][k-1] != '*':
            #cur_pos = cur_pos[h][k-1]
            k-=1
        elif walk_command[i].lower() == 'u' and h > 0 and the_grid[h-1][k] != '*':
            #cur_pos = cur_pos[h-1][k]
            h-=1
        else:
            h = h
            k = k
    return[h,k]



def generate_map(m, n, the_seed=0):
    if the_seed:
        random.seed(the_seed)
    the_map = [[random.choice([ALLOWED, FORBIDDEN]) for _ in range(n)] for _ in range(m)]
    the_map[0][0] = ALLOWED
    return the_map


def display_map(the_map):
    for i in range(len(the_map)):
        print(' '.join(the_map[i]))


if __name__ == '__main__':
    # clearly this next line of code is forbidden in general.

    the_map = generate_map(*list(map(int, input('Enter m n (optionally: seed): ').split())))
    display_map(the_map)
    move_command = input('What is the move command? ')
    print(walk_around(the_map, move_command))

