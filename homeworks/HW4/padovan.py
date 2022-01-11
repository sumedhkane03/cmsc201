"""
File:    padovan.py
Author:  Sumedh Kane
Date:    10/8/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  user enters a number which is a "goal". The program outputs how many steps of the Padovan Sequence
  it took to reach that "goal" integer.
"""
goal = int(input('Enter an integer "goal": '))

#pdv = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, 351, 465, 616, 816, 1081,
#1432, 1897, 2513, 3329, 4410, 5842, 7739, 10252, 13581, 17991, 23833, 31572, 41824, 55405, 73396, 97229, 128801, 170625]
pdv3 = 1
pdv2 = 1
pdv1 = 1
pdvCurrent = 2

count = 4
while pdvCurrent < goal:
    pdv1 = pdvCurrent
    pdvAdd = pdv3 + pdv2
    pdvCurrent = pdvAdd
    pdv3 = pdv2
    pdv2 = pdv1
    count += 1


print(count)
