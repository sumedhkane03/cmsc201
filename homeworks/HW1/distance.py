"""
File:    distance.py
Author:  Sumedh Kane
Date:    09/17/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program takes an input of two points on the coordinate plane (x1,y1) & (x2,y2)
  and outputs the distance between those two points.
"""
print('Hello please input the x1 value: ')
x1 = float(input())
print('Please input the y1 value: ')
y1 = float(input())
print('Please input the x2 value: ')
x2 = float(input())
print('Please input the y2 value: ')
y2 = float(input())

a = (x2-x1)**2
b = (y2-y1)**2

distance = (a+b)**0.5

print('The distance between the points (%s,%s) and (%s,%s) is %s' %(x1,y1,x2,y2,distance))
print('Thanks for using the distance calculator.')