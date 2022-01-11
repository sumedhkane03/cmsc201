"""
File:         names.py
Author:       Sumedh Kane
Date:         10/27/2021
Section:      41
E-mail:       sumedhk1@umbc.edu
Description:  YOUR DESCRIPTION GOES HERE AND HERE
              YOUR DESCRIPTION CONTINUED SOME MORE
"""


def sum_list(numbers):
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """
    sum = 0
    for i in numbers:
        sum+=i
    return sum


def get_string_lengths(strings):
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """
    long_strings = []
    for i in strings:
        long_strings.append(len(i))
    return long_strings


def get_names():
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """
    name = input('Enter a name enter stop to stop: ')
    all_names = []
    while name.lower() != 'stop':
        name = input('Enter a name enter stop to stop: ')
        all_names.append(name)
    return all_names

if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]
    print('There are ',sum_list(get_string_lengths(kitties)), ' letters in kitties.')
    # print the sum of the lengths of the strings in kitties

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]
    print('There are ',sum_list(get_string_lengths(puppers)), ' letters in puppers.')
    # prints the sum of the lengths of the strings in puppers

    # gets names from the user and reports how many letters are in all the names
    print('There are ',sum_list(get_string_lengths(get_names())), ' letters in all of the names you entered.')