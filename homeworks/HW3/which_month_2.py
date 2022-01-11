"""
File:    which_month_2.py
Author:  Sumedh Kane
Date:    09/24/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program takes an input of the month as an integer and how many months into the future that the user would like
  to go to. Version 2.
"""
if __name__ == '__main__':

    startingMonth = int(input("Please enter the current month as an integer (Jan-1,Feb-2,Mar-3, etc.): "))
    travelTime = int(input("Please enter the number of months you would like to travel forward in time (integer): "))


    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    finalMonth = ((startingMonth + travelTime) % 12) - 1
    print(months[finalMonth])







