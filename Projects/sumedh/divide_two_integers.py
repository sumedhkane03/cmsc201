def divide(dividend,divisor):
    neg = False
    count = 0
    ogDiv = abs(divisor)
    if (dividend * divisor) < 0:
        neg = True

    dividend = abs(dividend)
    divisor = abs(divisor)

    if ((dividend >= (2 ** 31) - 1) or (divisor >= (2 ** 31) - 1)):
        if neg:
            return -(2 ** 31) + 1
        else:
            return (2 ** 31) - 1
    elif ((dividend <= -(2 ** 31)+1) or (divisor <= -(2 ** 31) + 1)):
        if neg:
            return (2 ** 31) - 1
        else:
            return -(2 ** 31) + 1
    else:

        while True:
            if divisor <= dividend:
                count += 1
            else:
                break
            divisor += ogDiv
        if neg:
            count *= -1

        if count >= (2 ** 31):
            return 2 ** 31
        elif count <= -(2 ** 31):
            return -(2 ** 31)
        else:
            return count

if __name__ == '__main__':
    dividend = 7
    divisor = -3
    print(divide(dividend,divisor))