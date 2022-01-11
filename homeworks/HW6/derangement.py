


def derangement(number):
    if number == 0:
        answer = 1
    else:
        answer = (number * derangement(number-1)) + (-1)**number
    return answer





if __name__ == '__main__':
   for i in range(20):
       print(i, derangement(i))