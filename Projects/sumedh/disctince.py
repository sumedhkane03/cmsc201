def distinct(s):
    found = []
    for i in s:
        if i not in found:
            found.append(i)
    return len(found)



if __name__ == '__main__':
    s = str(input("enter string: "))
    print(distinct(s))