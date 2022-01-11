"""
File:    people_list.py
Author:  Sumedh Kane
Date:    10/1/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  runs a certain amount of steps and adds and removes poeple from a list
"""
if __name__ == '__main__':

    n = int(input("Enter number of steps to run: "))
    people_list = []
    for i in range(n):
        command = str(input("Enter command: "))
        x = command.split()
        if x[0].lower() == "add":
            people_list.append(x[1].lower())
            print(x[1], "added.")
        elif x[0].lower() == "remove":
            if people_list.count(x[1].lower()) == 0:
                print("Error Please Try again.")
            else:
                people_list.remove(x[1].lower())
                print(x[1], "removed")
        elif x[0].lower() == "max":
            print(max(people_list))
        elif x[0].lower() == "quit":
            break

        else:
            print("Error Please Try again.")

    print("Here is the final list: ", people_list)
