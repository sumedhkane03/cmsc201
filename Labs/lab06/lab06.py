"""
File:    circular.py
Author:  Sumedh Kane
Date:    THE DATE
Section: YOUR DISCUSSION SECTION NUMBER
E-mail:  YOUR_EMAIL@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""



rotator = str(input('Enter a string: ').lower())

rotator = rotator.split(sep=' ')
for i in rotator:
    i = i.strip('')

rotator = ''.join(rotator)

#print(rotator)

rotations = 0

for i in range(1,len(rotator)):
    if (rotator[i:] + rotator[:i]) == rotator:
        print(rotator,'is a rotation with offset',i)
        rotations+=1

if(rotations == 0):
        print('There are no rotations of the string')
'''
if u:
    print('y')
else:
    print('n')

  print(*rotator[(i+j) % len(rotator)],sep='\t')

'''
