"""
    Come up with a name for the game

    JMPs and HLTs
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c


def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)

def display_map(MAPSIZE,MAPSEED=0):
    the_grid = make_grid(MAPSIZE)
    loop_counter = 0
    for i in generate_random_map(MAPSIZE, MAPSEED):
        fill_grid_square(the_grid, MAPSIZE, loop_counter, i)
        loop_counter += 1

    for line in the_grid:
        print(''.join(line))

def action(MAPSIZE,MAPSEED):
    the_grid = make_grid(MAPSIZE)
    loop_counter = 0
    actions = []
    for i in generate_random_map(MAPSIZE, MAPSEED):
        fill_grid_square(the_grid, MAPSIZE, loop_counter, i)
        actions.append(i)
        loop_counter += 1
    return actions
def user_position():
    actions = action(MAPSIZE, MAPSEED)
    pos = roll_dice()
    if pos > len(actions) - 1:
        pos -= len(actions)

    score = 0
def security_check():
    if pos > len(actions) - 1:
        pos -= len(actions)

    while pos < len(actions):
        pos = roll_dice()

        if pos > len(actions)-1:
            pos -= len(actions)
        if pos > len(actions) - 1:
            pos -= len(actions)
        while actions[pos] != 'hlt':
            if pos > len(actions)-1:
                pos-=len(actions)
            pos = roll_dice()
            if pos > len(actions)-1:
                pos-=len(actions)
            print('POS: ', pos)
            if pos > len(actions)-1:
                pos-=len(actions)

            print('POSITION: ',actions[pos])
            if pos > len(actions)-1:
                pos-=len(actions)

            if 'jmp' in actions[pos]:
                amt = actions[pos].split()
                pos = int(amt[1])-2
                score = score
                pos+=roll_dice()
                print('POS: ', pos)
                if pos > len(actions) - 1:
                    pos -= len(actions)
            elif 'add' in actions[pos]:
                amt = actions[pos].split()
                score += int(amt[1])
                pos+=roll_dice()
                print('POS: ', pos)
                if pos > len(actions) - 1:
                    pos -= len(actions)

            elif 'sub' in actions[pos]:
                amt = actions[pos].split()
                score -= int(amt[1])
                pos+=roll_dice()
                print('POS: ', pos)
                if pos > len(actions) - 1:
                    pos -= len(actions)

            elif 'mul' in actions[pos]:
                amt = actions[pos].split()
                score *= int(amt[1])
                pos+=roll_dice()
                print('POS: ', pos)
                if pos > len(actions) - 1:
                    pos -= len(actions)

            elif 'nop' in actions[pos]:
                pos+=roll_dice()
                print('POS: ', pos)
                if pos > len(actions) - 1:
                    pos -= len(actions)

                score
            elif 'hlt' in actions[pos]:
                return score
            else:
                score
                pos+=roll_dice()
                print('POS: ', pos)
            if pos > len(actions)-1:
                pos-=len(actions)

        pos+=roll_dice()
        if pos > len(actions) - 1:
            pos -= len(actions)

        print('POS: ', pos)
    if pos > len(actions) - 1:
        pos -= len(actions)

    return score

def play_game(game_map=0):
    position = action(MAPSIZE,MAPSEED)
    #print(position)
    display_map(MAPSIZE,MAPSEED)
    print('Your Score is: ',user_position())

if __name__ == '__main__':
    MAPSIZE = int(input('Enter a size (integer) for the board: '))
    MAPSEED = int(input('Enter a seed (integer) for the board: '))
    play_game()

