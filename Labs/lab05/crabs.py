"""
File:         crabs.py
Author:       Sumedh Kane
Date:         10/6/2021
Section:      41
E-mail:       sumedhk1@umbc.edu
Description:  sorts out crabs by weight either light or heavy
"""


crabs = []
inp = ''
keep = []
doNotKeep = []
while inp.lower() != 'stop':
    inp = input('Enter weight of crab as a number (enter "stop" to stop): ')
    if inp.lower() == 'stop':
        print('stopped')
    elif inp.isalpha() or inp.isspace() or inp == '' or inp.isascii() or type.__getattribute__(inp) == str:
        print('Enter a number or "stop" please. ')
    else:
        crabs.append(float(inp))


met = False
while met == False:
    herd = input('Do you want to keep light or heavy crabs? ')
    if herd.lower() == 'light':
        minWeight = float(input('What weight determines whether a crab is light or heavy? '))
        met = True
    elif herd.lower() == 'heavy':
        minWeight = float(input('What weight determines whether a crab is light or heavy? '))
        met = True
    else:
        print('You must enter light or heavy: ')
        met = False

for i in crabs:
    if herd.lower() == 'light':
        if i < minWeight:
           if i % 1 == 0:
               i = int(i)
               keep.append(i)
           else:
               keep.append(i)
        else:
            if i % 1 == 0:
                i = int(i)
                doNotKeep.append(i)
            else:
                doNotKeep.append(i)
    else:
        if i > minWeight:
           if i % 1 == 0:
               i = int(i)
               keep.append(i)
           else:
               keep.append(i)
        else:
            if i % 1 == 0:
                i = int(i)
                doNotKeep.append(i)
            else:
                doNotKeep.append(i)
    i = float(i)




print('You will be keeping the crabs with weights: ', keep)
print('You will not be keeping the crabs with weights: ', doNotKeep)