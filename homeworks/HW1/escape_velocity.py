"""
File:    escape_velocity.py
Author:  Sumedh Kane
Date:    09/17/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
This program takes an input of a mass of a body and the radius of the body
"""

print('What body are we launching from?' )
body = str(input())
print('Enter the mass of the planet in scientific notation with the floating number first: ')
massFL = float(input())
print('What power of 10 is this? ')
massPower = int(input())

bodyMass = massFL * (10**massPower)

print('Enter the coefficient of the scientific notation of the radius from the center of Earth:')
radiusFL = float(input())
print('What power of 10 is this? ')
radiusPower = int(input())

radius = radiusFL * (10**radiusPower)

G = 6.67 * 10**-11
escNumerator = 2 * G * bodyMass
escVelocity = (escNumerator / radius)**0.5
escVelocity = round(escNumerator, 3)

print('The escape velocity required for %s is %s m/s' %(body,escVelocity))