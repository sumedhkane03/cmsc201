
def swap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1


# Prints all possibilities
def ab_equal(str, k, n):
    if k >= n:
        print(''.join(str))
        return
    for i in range(k, n):
        # Proceed further for str[i] only if it doesn't match with any of the characters after str[index]

        c = swap(str,k, i)
        if c:
            str[k], str[i] = str[i], str[k]
            ab_equal(str, k + 1, n)
            str[k], str[i] = str[i], str[k]

if __name__ == '__main__':
    n = int(input("Enter the Number of a's and b's to be printed: "))
    # if n is odd then it's not possible to print equal a's and b's

    if (n % 2 != 0):
        print("Not possible to print equal a's and b's as {} is and odd Number".format(n))

    else:
        # since it has to have n/2 number of a's and n/2 number of b's

        ch = 'a' * (n // 2) + 'b' * (n // 2)

        ab_equal(list(ch), 0,n)