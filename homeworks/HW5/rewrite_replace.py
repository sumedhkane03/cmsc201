"""
File:    rewrite_replace.py
Author:  Sumedh Kane
Date:    10/22/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  Takes a string input, finds a certain string within the string and replaces it with a specified third string.
"""
if __name__ == '__main__':

    the_string = str(input("What is the total string? ").lower())

    look_for = str(input("What string should we look for? ").lower())

    replace_with = str(input("What should we replace that string with? ").lower())

    '''
    def rewrite_replace(the_string,look_for,replace_with):
        result = ''

        taker = []
        for i in range(1,len(the_string)):
            if the_string[i] in look_for:
                taker.append(i)
            the_string[taker[0]:len(taker)] = replace_with


        return the_string
    '''

    def rewrite_replace(the_string, look_for, replace_with):
        result = ''
        j = 0
        k = 0
        '''
        if len(look_for) == 1:
            while j < len(look_for):

                for i in the_string:


                    if i == look_for:
                        i = replace_with
                    result = result + i
                j += 1
        '''
    #if len(look_for) > 1:

        while j < len(the_string):

            #print(the_string[j:j + k+1])
            y = the_string[j:j+len(look_for)]

            if the_string[j:j+len(look_for)] == look_for:
                #the_string[j:j+k] = replace_with
                x = the_string[:j]
                z = the_string[j+len(look_for):]

                the_string = the_string[:j] + replace_with + the_string[j+len(look_for):]

            j+=1




        return the_string


print(*rewrite_replace(the_string, look_for, replace_with),sep='')
