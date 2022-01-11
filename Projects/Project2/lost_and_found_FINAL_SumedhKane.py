"""
    Starter code for Lost and Found Project 2, CMSC 201 Fall 2021
"""

import json


USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'X'
DOOR = 'D'
SECRET = 'S'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'


def load_map(map_file_name):
    """
        When a map file name is passed the file will load the grid and return it.
        Should you modify this function? No you shouldn't.

    :param map_file_name: a string representing the file name.
    :return: a 2D list which contains the current map.
    """
    with open(map_file_name) as map_file:
        the_map = json.loads(map_file.read())

    return the_map


def print_map(the_map,start_pos):
    count=0
    rows=[]
    full_map = []
    if len(start_pos) > 0:
        for i in range(len(the_map)):
            rows = []
            count = 0
            for j in the_map[i]:
                count += 1

                if len(j['items']) > 0:
                    if [i,count-1] in start_pos:
                        rows.append('ጰ')
                    else:
                        rows.append('i')
                elif [i,count-1] in start_pos:
                    rows.append('ጰ')
                else:
                    if j['symbol'] == 's':
                        rows.append('*')
                    else:
                        rows.append(j['symbol'])


            full_map.append(rows)

            print(*rows, sep='')
    else:
        for i in range(len(the_map)):
            rows = []
            for j in the_map[i]:
                count += 1

                if len(j['items']) > 0:
                    if count == 1:
                        rows.append('ጰ')
                    else:
                        rows.append('i')
                elif count == 1:
                    rows.append('ጰ')
                else:
                    if j['symbol'] == 's':
                        rows.append('*')
                    else:
                        rows.append(j['symbol'])

            full_map.append(rows)

            print(*rows,sep='')

    return full_map


def print_full_map(full_map):
    rows = []
    for i in range(len(full_map)):
        rows = []
        for j in full_map[i]:
            rows.append(j)
        print(*rows,sep='')

def remove_prev_pos(full_map):
    for i in range(len(full_map)):
        for j in range(len(full_map[i])):
            if full_map[i][j] == 'ጰ':
                full_map[i][j] = '_'

def check_wall(full_map,player_move,y,x):
    if player_move == 'w':
        if full_map[y-1][x] == '*':
            return True
        elif full_map[y-1][x] == 'd':
            return True
        else:
            return False
    if player_move == 'a':
        if full_map[y][x-1] == '*':
            return True
        elif full_map[y][x-1] == 'd':
            return True
        else:
            return False
    if player_move == 's':
        if full_map[y+1][x] == '*':
            return True
        elif full_map[y+1][x] == 'd':
            return True
        else:
            return False
    if player_move == 'd':
        if full_map[y][x+1] == '*':
            return True
        elif full_map[y][x+1] == 'd':
            return True
        else:
            return False

def use(full_map,y,x,inventory,the_map):
    if y+1 < len(full_map):
        if full_map[y+1][x] == 'd':
            if 'requires' in the_map[y + 1][x]:
                if the_map[y+1][x]['requires'] in inventory:
                    full_map[y + 1][x] = '_'
            else:
                full_map[y + 1][x] = '_'
        if the_map[y+1][x]['symbol'] == 's':
            if the_map[y+1][x]['symbol'] == 's':
                full_map[y + 1][x] = 'd'
                the_map[y + 1][x]['symbol'] = 'd'
    if y-1 >= 0:
        if full_map[y-1][x] == 'd':

            if 'requires' in the_map[y - 1][x]:
                if the_map[y-1][x]['requires'] in inventory:
                    full_map[y - 1][x] = '_'
            else:
                full_map[y - 1][x] = '_'
        if the_map[y-1][x]['symbol'] == 's':
            if the_map[y-1][x]['symbol'] == 's':
                full_map[y - 1][x] = 'd'
                the_map[y - 1][x]['symbol'] = 'd'
    if x+1 < len(full_map[0]):
        if full_map[y][x+1] == 'd':

            if 'requires' in the_map[y][x + 1]:
                if the_map[y][x+1]['requires'] in inventory:
                    full_map[y][x + 1] = '_'
            else:
                full_map[y][x+1] = '_'
        if the_map[y][x+1]['symbol'] == 's':
            if the_map[y][x+1]['symbol'] == 's':
                full_map[y][x+1] = 'd'
                the_map[y][x + 1]['symbol'] = 'd'
    if x-1 >= 0:
        if full_map[y][x-1] == 'd' :
            if 'requires' in the_map[y][x - 1]:
                if the_map[y][x-1]['requires'] in inventory:
                    full_map[y][x - 1] = '_'
            else:
                full_map[y][x-1] = '_'
        if the_map[y][x-1]['symbol'] == 's':
            if the_map[y][x-1]['symbol'] == 's':
                full_map[y][x-1] = 'd'
                the_map[y][x - 1]['symbol'] = 'd'
    if y+1 < len(full_map) and x-1 >= 0:
        if full_map[y+1][x-1] == 'd':
            if 'requires' in the_map[y + 1][x - 1]:
                if the_map[y+1][x-1]['requires'] in inventory:
                    full_map[y+1][x - 1] = '_'
            else:
                full_map[y + 1][x-1] = '_'
        if the_map[y][x-1]['symbol'] == 's':
            if the_map[y+1][x-1]['symbol'] == 's':
                full_map[y + 1][x-1] = 'd'
                the_map[y + 1][x - 1]['symbol'] = 'd'
    if y+1 < len(full_map) and x+1 < len(full_map[0]):
        if full_map[y+1][x+1] == 'd':
            if 'requires' in the_map[y + 1][x + 1]:
                if the_map[y+1][x+1]['requires'] in inventory:
                    full_map[y+1][x + 1] = '_'
            else:
                full_map[y + 1][x+1] = '_'
        if the_map[y][x-1]['symbol'] == 's':
            if the_map[y+1][x+1]['symbol'] == 's':
                full_map[y + 1][x+1] = 'd'
                the_map[y + 1][x + 1]['symbol'] = 'd'
    if y-1 >= 0 and x-1 >= 0:
        if full_map[y-1][x-1] == 'd':
            if 'requires' in the_map[y - 1][x - 1]:
                if the_map[y-1][x-1]['requires'] in inventory:
                    full_map[y-1][x - 1] = '_'
            else:
                full_map[y - 1][x-1] = '_'
        if the_map[y][x-1]['symbol'] == 's':
            if the_map[y-1][x-1]['symbol'] == 's':
                full_map[y - 1][x-1] = 'd'
                the_map[y - 1][x - 1]['symbol'] = 'd'
    if y-1 >= 0 and x+1 < len(full_map[0]):
        if full_map[y-1][x+1] == 'd':
            if 'requires' in the_map[y-1][x+1]:
                if the_map[y-1][x+1]['requires'] in inventory:
                    full_map[y-1][x + 1] = '_'
            else:
                full_map[y - 1][x+1] = '_'
        if the_map[y][x-1]['symbol'] == 's':
            if the_map[y-1][x+1]['symbol'] == 's':
                full_map[y - 1][x+1] = 'd'
                the_map[y - 1][x + 1]['symbol'] = 'd'
def find_start(the_map):
    start_pos = []
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            for key in the_map[i][j]:
                if key == 'start':
                    start_pos.append([i, j])
    return start_pos

def find_item_coords(the_map):
    items = []
    for i in range(len(the_map)):
        for j in range(len(the_map[i])):
            for key in the_map[i][j]:
                if len(the_map[i][j]['items']) > 0:
                    items.append([i,j])
    return items

def move_player(full_map,items,the_map,start_pos):
    num_of_columns = len(full_map)
    num_of_rows = len(full_map[0])
    if len(start_pos) > 0:
        y = start_pos[0][0]
        x = start_pos[0][1]
    else:
        x = 0
        y = 0
    current_position = full_map[y][x]
    full_map[y][x] = 'ጰ'
    player_move = input("Enter (wasd) to move or 'quit' to quit : ")
    player_move.lower()
    inventory = []
    if [y,x] in items:
        inventory.append(the_map[y][x]['items'])

    while player_move != 'quit' and current_position != 'x':
        if len(player_move) > 1:
            player_move = player_move[0]
        if player_move == 'w':
            if y-1 >= 0:
                if not check_wall(full_map,player_move,y,x):
                    if full_map[y-1][x] == 'x':
                        print('You win!')
                        current_position = 'x'
                        player_move = 'quit'
                    else:
                        if y - 1 >= 0:
                            y -= 1
                            if [y,x] in items:
                                inventory.append(the_map[y][x]['items'])
                            remove_prev_pos(full_map)
                            full_map[y][x] = 'ጰ'
                            print(f'Current position is: ({x},{y})')

                            print_full_map(full_map)
                            print("Inventory: ", *inventory, sep='')
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                        else:
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                else:
                    remove_prev_pos(full_map)
                    full_map[y][x] = 'ጰ'
                    print(f'Current position is: ({x},{y})')

                    print_full_map(full_map)
                    print("Inventory: ", *inventory, sep='')
                    player_move = input("Enter (wasd) to move or 'quit' to quit : ")
            else:
                full_map[y][x] = 'ጰ'
                print(f'Current position is: ({x},{y})')
                print_full_map(full_map)
                print("Inventory: ", *inventory, sep='')
                player_move = input("Enter (wasd) to move or 'quit' to quit : ")
        elif player_move == 'a':
            if x-1 >= 0:
                if not check_wall(full_map,player_move,y,x):
                    if full_map[y][x-1] == 'x':
                        print('You win!')
                        player_move = 'quit'
                        current_position = 'x'
                    else:
                        if x - 1 < num_of_rows:
                            x -= 1
                            if [y,x] in items:
                                inventory.append(the_map[y][x]['items'])
                            remove_prev_pos(full_map)
                            full_map[y][x] = 'ጰ'
                            print(f'Current position is: ({x},{y})')

                            print_full_map(full_map)
                            print("Inventory: ", *inventory, sep='')
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                        else:
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                else:
                    remove_prev_pos(full_map)
                    full_map[y][x] = 'ጰ'
                    print(f'Current position is: ({x},{y})')

                    print_full_map(full_map)
                    print("Inventory: ", *inventory, sep='')
                    player_move = input("Enter (wasd) to move or 'quit' to quit : ")
            else:
                full_map[y][x] = 'ጰ'
                print(f'Current position is: ({x},{y})')

                print_full_map(full_map)
                print("Inventory: ", *inventory, sep='')
                player_move = input("Enter (wasd) to move or 'quit' to quit : ")

        elif player_move == 's':
            if y+1 < len(full_map):
                if not check_wall(full_map,player_move,y,x):
                    if full_map[y+1][x] == 'x':
                        print('You win!')
                        player_move = 'quit'
                        current_position = 'x'
                    else:
                        if y+1 < num_of_rows:
                            y += 1
                            if [y,x] in items:
                                inventory.append(the_map[y][x]['items'])
                            remove_prev_pos(full_map)
                            full_map[y][x] = 'ጰ'
                            print(f'Current position is: ({x},{y})')

                            print_full_map(full_map)
                            print("Inventory: ", *inventory, sep='')
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                        else:
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                else:
                    remove_prev_pos(full_map)
                    full_map[y][x] = 'ጰ'
                    print(f'Current position is: ({x},{y})')

                    print_full_map(full_map)
                    print("Inventory: ", *inventory, sep='')
                    player_move = input("Enter (wasd) to move or 'quit' to quit : ")
            else:
                full_map[y][x] = 'ጰ'
                print(f'Current position is: ({x},{y})')

                print_full_map(full_map)
                print("Inventory: ", *inventory, sep='')
                player_move = input("Enter (wasd) to move or 'quit' to quit : ")

        elif player_move == 'd':
            if x+1 < len(full_map[0]):
                if not check_wall(full_map,player_move,y,x):
                    if full_map[y][x+1] == 'x':
                        print('You win!')
                        player_move = 'quit'
                        current_position = 'x'
                    else:
                        if x + 1 < num_of_rows:
                            x += 1
                            if [y,x] in items:
                                inventory.append(the_map[y][x]['items'])
                            remove_prev_pos(full_map)
                            full_map[y][x] = 'ጰ'
                            print(f'Current position is: ({x},{y})')

                            print_full_map(full_map)
                            print("Inventory: ", *inventory, sep='')
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                        else:
                            player_move = input("Enter (wasd) to move or 'quit' to quit : ")
                else:
                    remove_prev_pos(full_map)
                    full_map[y][x] = 'ጰ'
                    print(f'Current position is: ({x},{y})')

                    print_full_map(full_map)
                    print("Inventory: ", *inventory, sep='')
                    player_move = input("Enter (wasd) to move or 'quit' to quit : ")
            else:
                full_map[y][x] = 'ጰ'
                print(f'Current position is: ({x},{y})')

                print_full_map(full_map)
                print("Inventory: ", *inventory, sep='')
                player_move = input("Enter (wasd) to move or 'quit' to quit : ")
        elif player_move == 'e':
            use(full_map,y,x,inventory,the_map)
            remove_prev_pos(full_map)
            full_map[y][x] = 'ጰ'
            print(f'Current position is: ({x},{y})')
            print_full_map(full_map)
            print("Inventory: ", *inventory, sep='')
            player_move = input("Enter (wasd) to move or 'quit' to quit : ")

        else:
            current_position = full_map[y][x]
            print('Current position is: ', current_position)
            player_move = input("Enter (wasd) to move or 'quit' to quit : ")



def play_game(the_game_map):
    # print_map(the_game_map)
    move_player(print_map(the_game_map,find_start(the_game_map)),find_item_coords(the_game_map),the_game_map,find_start(the_game_map))


if __name__ == '__main__':
    map_file_name = input('What map do you want to load? ')
    #map_file_name = 'second_map.map'
    the_game_map = load_map(map_file_name)
    if the_game_map:
        play_game(the_game_map)
        pass
    #print(find_start(the_game_map))
