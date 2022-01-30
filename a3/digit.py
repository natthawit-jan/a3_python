def kthDigit(x: int, b: int, k: int):
    while x > 0 or k > 0:
        if k == 0:
            return x % b
        x //= b
        k -= 1
    return 0


# make a version without using a loop
def kthDigitVersion2(x: int, b: int, k: int):
    return x // (b ** k) % b if k >= 0 else 0


assert kthDigitVersion2(789, 10, 1) == 8
assert kthDigitVersion2(789, 10, 2) == 7
assert kthDigitVersion2(789, 10, 3) == 0
assert kthDigitVersion2(789, 10, 0) == 9
assert kthDigitVersion2(789, 10, -3) == 0

assert kthDigitVersion2(987, 16, 0) == 11
assert kthDigitVersion2(987, 16, 1) == 13
assert kthDigitVersion2(987, 16, 2) == 3
assert kthDigitVersion2(987, 16, 3) == 0
assert kthDigitVersion2(987, 16, 4) == 0
assert kthDigitVersion2(987, 16, -323) == 0
# def pp(ch: str):
#     print(ch, end='')
#
#
# def a():
#     pp('a')
#
#
# def b():
#     pp('b')
#
#
# def c():
#     a()
#     pp('c')
#
#
# def d():
#     pp('d')
#     b()
#
#
# def e():
#     """
#     d
#     """
#     c()
#     pp('e')
#     d()
#
#
# import itertools
#
# list_of_func = [a,b,c,d,e]
#
# all_possible_outcome = list(itertools.permutations(list_of_func, 5))
#
# for i in all_possible_outcome:
#     print(i)
#     for j in i:
#         j()
#     print()
