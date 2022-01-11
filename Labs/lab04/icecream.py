"""
File:         icecream.py
Author:       Sumedh Kane
Date:         9/29/2019
Section:      41
E-mail:       sumedhk1@umbc.edu
Description: loops through lists of icecream flavors and toppings

"""
if __name__ == "__main__":

    ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
    toppings = ["caramel", "marshmallow", "gummi bears"]

    for flavors in ice_cream_flavors:
        for things in toppings:
            print("%s is tasty with %s" %(flavors,things))
        if flavors == "strawberry":
            print("Strawberry is my favorite flavor!")