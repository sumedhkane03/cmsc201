"""
File:    factor_me.py
Author:  Sumedh Kane
Date:    10/8/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  takes a user input of an integer and outputs all of its prime number factors
"""
if __name__ == '__main__':

    orig = int(input("Enter an integer to be factored: "))
    x = orig
    factors = []
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for i in primes:

        while x % i == 0:
         #   if x % i == 0:
            factors.append(i)
            x = x / i
    if x > 50:
        x = int(x)
        print("The factors of %s are:" %(orig),)
        print(*factors, sep="*")
        print("There is however a factor of %s that is greater than 50, it is %s" %(orig,x))
    else:
        print(*factors, sep = "*")


#PREVIOUS CODE THAT I SHORTENED :)
    """
    while x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0 or x % 13 == 0 or x % 17 == 0 or x % 19 == 0 or x % 23 == 0 or x % 29 == 0 or x % 31 == 0 or x % 37 == 0 or x % 41 == 0 or x % 43 == 0 or x % 47 == 0:

        if x % 2 == 0:
            factors.append(2)
            x = x / 2
        elif x % 3 == 0:
            factors.append(3)
            x = x / 3
        elif x % 7 == 0:
            factors.append(7)
            x = x / 7
        elif x % 11 == 0:
            factors.append(11)
            x = x / 11
        elif x % 5 == 0:
            factors.append(5)
            x = x / 5
        elif x % 13 == 0:
            factors.append(13)
            x = x / 13
        elif x % 17 == 0:
            factors.append(17)
            x = x / 17
        elif x % 19 == 0:
            factors.append(19)
            x = x / 19
        elif x % 23 == 0:
            factors.append(23)
            x = x / 23
        elif x % 29 == 0:
            factors.append(29)
            x = x / 29
        elif x % 31 == 0:
            factors.append(31)
            x = x / 31
        elif x % 37 == 0:
            factors.append(37)
            x = x / 37
        elif x % 41 == 0:
            factors.append(41)
            x = x / 41
        elif x % 47 == 0:
            factors.append(47)
            x = x / 47
        elif x % 43 == 0:
            factors.append(43)
            x = x / 43
        """