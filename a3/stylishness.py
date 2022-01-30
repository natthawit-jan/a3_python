def got_table(you: int, date: int) -> str:
    if (2 < you < 8 and date >= 8) or (you >= 8 and (date >= 8 or 2 < date < 8)):
        return 'yes'
    elif 2 < you < 8 and 2 < date < 8:
        return 'maybe'
    else:
        return 'no'


assert got_table(7, 3) == 'maybe'
assert got_table(9, 4) == 'yes'
assert got_table(7, 8) == 'yes'
assert got_table(1, 10) == 'no'
assert got_table(5,4) == 'maybe'
assert got_table(5,8) == 'yes'
assert got_table(4, 10) == 'yes'
assert got_table(2, 2) == 'no'
assert got_table(10, 10) == 'yes'
assert got_table(3, 3) == 'maybe'
