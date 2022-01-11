"""
File:    ab_verify.py
Author:  SUMEDH KANE
Date:    12/3/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  i tried :(
"""

'''
def ab_verify(s,n=0):
    max_concur = 0
    if len(s) == 0:
        return n
    if s[0] == 'a':
        n+=1
    elif s[0] == 'b':
        n-=1
    ab_verify(s[1:len(s)],n)
    if n >= 0:
        return True
    else:
        return False


def ab_verify(s,n):
    if len(s) == 0:
        return n
    if type(n) == int:
        if s[0] == 'a':
            n = True
        elif s[0] == 'b':
            n = False
        max_concur = 0
        concurrent = 0
    if s[0] == 'a':
        n = True
    elif s[0] == 'b':
        n = True
'''
def ab_verify(verify, count=0,a=0,b=0):
    if count == 0:
        a = 0
        b = 0
        count+=1
    if len(verify) != 0:
        if verify[0] == 'a':
            a+=1
        if verify[0] =='b':
            b+=1
        ab_verify(verify[1:len(verify)],count,a,b)
    else:
        if a >= b:
            return True
        else:
            return False
'''
NON RECURSIVE BUT PRETTY MUCH WORKS

def ab_verify(verify, count):
    a = 0
    b = 0
    for i in verify:
        if i == 'a':
            a+=1
        if i =='b':
            b+=1
    if a>= b:
        return True
    else:
        return False
'''
def ab_veddrify(s,n=0):
    if len(s) == 0:
        return n

    if s[0] == 'a':
        n += 1
    elif s[0] == 'b':
        n -= 1

    abv(s[1:len(s)], n)


    if n>=0:
        return True
    elif n<0:
        return False
    return n

if __name__ == '__main__':
    #I tried but unfortunately ran out ot time :\
    s = input('Enter a string to test: ')
    while s != 'quit':
       print(ab_verify(s, 0))
       s = input('Enter a string to test: ')