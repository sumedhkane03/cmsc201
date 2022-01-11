"""
File:    list_reverse.py
Author:  Sumedh Kane
Date:    10/8/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  user enters a list seperated by commas, the program removes any entries with numbers, then outputs the new list
  in reverse order
"""
x = input("Enter a string seperated by commas: ")
x = x.lower().split(',')
printing = []
final = []

for i in range(len(x)):
    y = x[i]
    
    if y.isalpha() == True:
        printing.append(y)

for j in range(len(printing),0,-1):
    final.append(printing[j-1])

print(*final,sep=',')







#OLD CODE DOESNT WORK
"""
x = input("Enter a string seperated by commas: ")
x = x.lower().split(',')

numbers = ['1','2','3','4','5','6','7','8','9']
final = []
executive = []
for i in range(len(x)):
    for j in x[i]:
        k = x[i]
        if numbers.count(j) > 0:
            final.append(k)
for y in x:

    if final.count(y) == 0:
        executive.append(x)
print(executive)
"""