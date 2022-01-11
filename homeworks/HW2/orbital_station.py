"""
File:    orbital_station.py
Author:  Sumedh Kane
Date:    09/24/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  This program asks the user if it wants to control the orbital speed or the station radius. Then performs calculations
  based on user response.
"""

control = str(input('Would you like to control "rotation speed" or "station radius"? ').lower())
if (control == "rotation speed"):
    radius = float(input('What is the radius of the station? '))
    RPM = (60 / (2 * 3.141592)) * ((9.8 / radius)**0.5)
    print("The rotation speed is %s rpm" %(RPM))
elif (control == "station radius"):
    stationRPM = float(input("What speed in rpm do you want the station to rotate?"))
    stationRadius = 9.8 / (((2 * 3.141592 * stationRPM) / 60)**2)
    print("The radius of the station is %s meters." %(stationRadius))
else:
    print("Please enter either 'rotation speed' or 'station radius' and try again.")
