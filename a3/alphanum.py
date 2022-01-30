def phoneWord2Num(word: str) -> int:
    def getCode(letter):
        if letter in 'abcABC':
            return '2'
        elif letter in 'defDEF':
            return '3'
        elif letter in 'ghiGHI':
            return '4'
        elif letter in 'jklJKL':
            return '5'
        elif letter in 'monMON':
            return '6'
        elif letter in 'pqrsPQRS':
            return '7'
        elif letter in 'tuvTUV':
            return '8'
        else:
            return '9'

    result = ""
    result += getCode(word[0])
    result += getCode(word[1])
    result += getCode(word[2])
    result += getCode(word[3])
    result += getCode(word[4])
    result += getCode(word[5])
    result += getCode(word[6])

    return int(result)

assert phoneWord2Num('FLOWERS') == 3569377
assert phoneWord2Num('PrOGrAM') == 7764726
assert phoneWord2Num('Battery') == 2288379