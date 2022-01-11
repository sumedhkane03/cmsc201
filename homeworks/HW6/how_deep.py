import random


def make_list_structure(max_depth, p=.8):
   if max_depth and random.random() < p:
       new_list = []
       for i in range(5):
           sub_list = make_list_structure(max_depth - 1, p * .9)
           if sub_list is not None:
               new_list.append(sub_list)
       return new_list
   return None

def how_deep(deepest):
    super = []
    max = 0
    for i in deepest:
        super.append(how_deep(i))

    if len(deepest) == 0:
        return 1
    else:
        for value in super:
            if value > max:
                max = value
        return max + 1


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))

