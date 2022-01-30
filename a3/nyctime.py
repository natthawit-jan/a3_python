def nycHour(bkkHour: int) -> str:
    subtraction = bkkHour - 11
    ny_time_24_format = 24 + subtraction if subtraction < 0 else subtraction
    pm_am = "am" if 12 > ny_time_24_format >= 0 else "pm"
    # special case
    return '12' + pm_am if ny_time_24_format == 0 or ny_time_24_format == 12 else str(ny_time_24_format % 12) + pm_am


assert nycHour(0) == "1pm"
assert nycHour(1) == "2pm"
assert nycHour(2) == "3pm"
assert nycHour(3) == "4pm"
assert nycHour(4) == "5pm"
assert nycHour(5) == "6pm"
assert nycHour(6) == "7pm"
assert nycHour(7) == "8pm"
assert nycHour(8) == "9pm"
assert nycHour(9) == "10pm"
assert nycHour(10) == "11pm"
assert nycHour(11) == "12am"
assert nycHour(12) == "1am"
assert nycHour(13) == "2am"
assert nycHour(14) == "3am"
assert nycHour(15) == "4am"
assert nycHour(16) == "5am"
assert nycHour(17) == "6am"
assert nycHour(18) == "7am"
assert nycHour(19) == "8am"
assert nycHour(20) == "9am"
assert nycHour(21) == "10am"
assert nycHour(22) == "11am"
assert nycHour(23) == "12pm"


