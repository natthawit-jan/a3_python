def price(vol: int):
    if 0 < vol < 20:
        return 18. * vol + 250.0
    elif 20 <= vol <= 100:
        return 18. * vol + vol * 10.
    elif vol > 100:
        sub_tol = vol * 18.
        disc = sub_tol * 0.01
        return vol * 18. - disc
    else:
        return 0.


# test cases
assert price(5) == 340.
assert price(20) == 560.
assert price(0) == 0.
assert price(200) == 3564.0
