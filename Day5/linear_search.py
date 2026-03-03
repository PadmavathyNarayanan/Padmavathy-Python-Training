import sys


li = sys.argv[1].replace('[','').replace(']','').split(',')
li = [int(i) for i in li]
target = int(sys.argv[2])


def linear_search(input_li: list, target: int) -> int:
    print(input_li, target)
    for i, j in enumerate(input_li):
        if j == target:
            return i
    return -1


print(linear_search(li, target))