"""
File:    lottery.py
Author:  Sumedh Kane
Date:    10/22/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  Takes user input of their own and the winning lottery ticket, then outputs the amount of money won.
"""
from random import randint, sample

winningTicket = [[]]
winningInput = []
userTicket = [[]]
userInput = []
count = 0


winningInput.append(str(input("Enter the winning ticket, put the powerball last: \n")).split(sep=" "))

userInput.append(str(input("Enter your ticket, put the powerball last: \n")).split(sep=" "))

for i in range(len(winningInput)):
    for j in winningInput[i]:
        j = int(j)
        count+=1
        if count < 7:
            if count == 6:
               winningTicket.append(j)
            else:
              winningTicket[0].append(j)
count = 0



for i in range(len(userInput)):
    for j in userInput[i]:
        j = int(j)
        count+=1
        if count < 7:
            if count == 6:
               userTicket.append(j)
            else:
              userTicket[0].append(j)
count = 0
#print('Winning Ticket is: ', winningTicket)
#print('User Ticket is: ', userTicket)


GP = int(input("What is the Grand Prize? "))


def check_ticket(userTicket,winningTicket,GP):
    match = 0
    winnings = 0
    if winningTicket[1] == userTicket[1]:
        for k in winningTicket[0]:
            if k in userTicket[0]:
                match+=1
        if match == 0 or match == 1:
            winnings = 4
        elif match == 2:
            winnings = 7
        elif match == 3:
            winnings = 100
        elif match == 4:
            winnings = 50000
        else:
            winnings = GP
    else:
        for k in winningTicket[0]:
            if k in userTicket[0]:
                match+=1
        if match == 0 or match == 1 or match == 2:
            winnings = 0
        elif match == 3:
            winnings = 7
        elif match == 4:
            winnings = 100
        else:
            winnings = '1,000,000'
    print('You win: $%s'%(winnings))


check_ticket(userTicket,winningTicket,GP)
