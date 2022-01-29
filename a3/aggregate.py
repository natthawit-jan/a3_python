from random import random


def my_min(p: float, q: float, r: float):
    return p if r > p < q else q if q < r else r


def my_mean(p: float, q: float, r: float):
    return (p + q + r) / 3.

def my_med(p: float, q: float, r: float):
    _my_min = my_min(p, q, r)
    if _my_min == p:
        return q if r >= q else r
    elif _my_min == q:
        return p if r >= p else r
    else:
        return q if p >= q else p


for i in range(100):
    a, b, c = random(), random(), random()
    assert my_min(a, b, c) == min((a, b, c))
    print(a,b,c)
    print(my_med(a,b,c))
    assert my_med(a, b, c) == sorted((a,b,c))[1]

