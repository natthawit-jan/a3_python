def kthDigit(x: int, b: int, k: int):
    while x > 0 or k > 0:
        if k == 0:
            return x % b
        x //= b
        k -= 1
    return 0


# make a version without using a loop

def pp(ch: str):
    print(ch, end='')


def a():
    pp('a')


def b():
    pp('b')


def c():
    a()
    pp('c')


def d():
    pp('d')
    b()


def e():
    """
    d
    """
    c()
    pp('e')
    d()


import itertools

list_of_func = [a,b,c,d,e]

all_possible_outcome = list(itertools.permutations(list_of_func, 5))

for i in all_possible_outcome:
    print(i)
    for j in i:
        j()
    print()
