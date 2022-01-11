def print_favorite_numbers(who, favorites):
    """
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """
    if who in favorites:
        print(favorites[who])
    else:
        print('Person not in favorites.')
    pass


def add_favorite_number(who, number, favorites):
    """
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """
    stop = 0
    if who not in favorites:
        favorites[who] = []
        print(f'empty list added for: {who}')

    for key in favorites:
        if number in favorites[key]:
            stop +=1
    if stop == 0:
        favorites[who].append(number)
        print(f"{num} was added to {who}'s favorites")


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            who, num = in_string.split()
            num = int(num)
            add_favorite_number(who, num, favorites)


        in_string = input('What do you want to do (add favorite number), or quit? ')

#print(favorites)
