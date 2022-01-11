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
def to_do_list(MAPSIZE,MAPSEED):
    #generates list of actions by index/position of the player
    toDo = []
    for i in generate_random_map(MAPSIZE, MAPSEED):
        toDo.append(i)

    return toDo

def work_the_player(MAPSIZE,MAPSEED,toDo):
    #calculates and prints all moves made by the player
    pos = 0
    score = 0
    count = 0
    move = 0
    pm = 0
    line_number = 0
    jumped = False
    add = False
    nop = False
    mul = False
    sub = False
    while 'hlt' not in toDo[pm]:


        move = roll_dice()
        last_roll = move
        pm = pos + move
        while pm >= len(toDo):
            #move = roll_dice()
            pm = pm % len(toDo)
            pos = pm
            move = 0
        line_number += 1
        jumped = False

        while pm >= len(toDo):
            #move = roll_dice()
            pm = pm % len(toDo)
            pos = pm
            move = 0




        print('')
        if 'jmp' in toDo[pm]:
            print(f'{line_number}. Pos: {pm} Score: {score} Instruction: {toDo[pm]} Rolled: {last_roll}')
            nyum = []
            nyum = toDo[pm].split()
            move = 0

            pm = int(nyum[1])
            pos = pm
            jumped = True


        elif 'nop' in toDo[pm]:

            pos += move
            move = 0
            #pm = pos + move
            nop = True

        elif 'add' in toDo[pm]:

            nyum = []
            nyum = toDo[pm].split()
            score += int(nyum[1])
            pos = pm
            add = True
        elif 'sub' in toDo[pm]:

            nyum = []
            nyum = toDo[pm].split()
            score -= int(nyum[1])
            pos = pm
            sub = True
        elif 'mul' in toDo[pm]:

            nyum = []
            nyum = toDo[pm].split()
            score *= int(nyum[1])
            pos = pm
            mul = True


        if jumped:
            print('\n')
            line_number+=1

        print(f'{line_number}. Pos: {pm} Score: {score} Instruction: {toDo[pm]} Rolled: {last_roll}')



        count += 1

        if count > 1000000:
            toDo[pos+move] = 'hlt'
    print(f'Your score is: {score}')

def print_grid(MAPSIZE,MAPSEED):
    #prints out the grid with the instructions in the boxes
    the_grid = make_grid(MAPSIZE)
    loop_counter = 0
    for i in generate_random_map(MAPSIZE, MAPSEED):
        fill_grid_square(the_grid, MAPSIZE, loop_counter, i)
        loop_counter += 1

    for line in the_grid:
        print(''.join(line))

def play_game(game_map):
    #plays the game by calling all other functions

    bss_split = board_size_and_seed.split(sep=' ')
    MAPSIZE = int(bss_split[0])
    MAPSEED = int(bss_split[1])
    print_grid(MAPSIZE,MAPSEED)
    work_the_player(MAPSIZE,MAPSEED,to_do_list(MAPSIZE,MAPSEED))


if __name__ == '__main__':
    board_size_and_seed = input("Enter the map size and seed or 'quit' to stop: ")
    while board_size_and_seed.lower() != 'quit':
        play_game(board_size_and_seed)
        board_size_and_seed = input("Enter the map size and seed or 'quit' to stop: ")
    print("Thank you for playing!")


