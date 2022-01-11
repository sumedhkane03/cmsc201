"""
File:    five_myths.py
Author:  Sumedh Kane
Date:    10/1/2021
Section: 41
E-mail:  sumedhk1@umbc.edu
Description:
  sorts out myths about a subject. all given by user
"""
if __name__ == '__main__':

    subject = str(input("Tell me the subject: "))
    myth1 = str(input("Tell me a myth about " + subject + ": "))
    myth2 = str(input("Tell me a myth about " + subject + ": "))
    myth3 = str(input("Tell me a myth about " + subject + ": "))
    myth4 = str(input("Tell me a myth about " + subject + ": "))
    myth5 = str(input("Tell me a myth about " + subject + ": "))

    isMyth1 = str(input("Is it actually a myth that " + myth1 + ": ").lower())
    isMyth2 = str(input("Is it actually a myth that " + myth2 + ": ").lower())
    isMyth3 = str(input("Is it actually a myth that " + myth3 + ": ").lower())
    isMyth4 = str(input("Is it actually a myth that " + myth4 + ": ").lower())
    isMyth5 = str(input("Is it actually a myth that " + myth5 + ": ").lower())

    truth = []
    lie = []
    areMyths = [isMyth1,isMyth2,isMyth3,isMyth4,isMyth5]
    myths = [myth1,myth2,myth3,myth4,myth5]
    for i in range(5):
        if areMyths[i] == "yes":
            lie.append(myths[i])
        else:
            truth.append(myths[i])
    print("Here are the myths: ", lie)
    print("Here are the non-myths which shouldn't have been included: ", truth)