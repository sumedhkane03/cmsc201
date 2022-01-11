"""
File:    burger.py
Author:  Sumedh Kane
Date:    10/8/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  takes user input and builds a burger, then prints the description of that burger
"""
if __name__ == '__main__':


    addOn = ""
    burger = ['bottom bun']
    condiments = []

    print("Start building your burger, enter 'top bun' when finished. ")
    print("What would you like to add onto the burger? bottom bun")
    while addOn.lower() != 'top bun':
        addOn  = input("What would you like to add onto the burger? ")
        if addOn == 'patty':
            addOn = 'burger'
        burger.append(addOn.lower())

    burger.remove("top bun")
    burger.remove('bottom bun')
    while burger.count('cheese') > 0:
        burger.remove('cheese')
    while burger.count('burger') > 0:
        burger.remove('burger')
    if(burger.count("cheese") > 0):
        print("You have created a %s-cheese cheeseburger." %(burger.count('cheese')))

    elif burger.count("burger") > 0:
        print("You have created a %s-burger hamburger." %(burger.count("burger")))

    else:
        print("You have created a burger.")
    print("The condiments you used were: ")
    print(*burger, sep = ", ")

