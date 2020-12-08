Base64_table = {
    0: 'A', 16: 'Q', 32: 'g', 48: 'w',
    1: 'B', 17: 'R', 33: 'h', 49: 'x',
    2: 'C', 18: 'S', 34: 'i', 50: 'y',
    3: 'D', 19: 'T', 35: 'j', 51: 'z',
    4: 'E', 20: 'U', 36: 'k', 52: '0',
    5: 'F', 21: 'V', 37: 'l', 53: '1',
    6: 'G', 22: 'W', 38: 'm', 54: '2',
    7: 'H', 23: 'X', 39: 'n', 55: '3',
    8: 'I', 24: 'Y', 40: 'o', 56: '4',
    9: 'J', 25: 'Z', 41: 'p', 57: '5',
    10: 'K', 26: 'a', 42: 'q', 58: '6',
    11: 'L', 27: 'b', 43: 'r', 59: '7',
    12: 'M', 28: 'c', 44: 's', 60: '8',
    13: 'N', 29: 'd', 45: 't', 61: '9',
    14: 'O', 30: 'e', 46: 'u', 62: '+',
    15: 'P', 31: 'f', 47: 'v', 63: '/'
}

octest_to_str = lambda x: str(chr(x))
str_to_octes = lambda x: ord(x)
get_bin = lambda x, n: format(x, 'b').zfill(n)
to_int = lambda x: int(x, 2)
get_key = lambda x: next((key for key, value in Base64_table.items() if value == x), None)


def to_base_64(string):
    octests_list = [str_to_octes(x) for x in string]
    bits = ''.join([get_bin(x, 8) for x in octests_list])
    sextets_list = [to_int(x) for x in _to_sextets_bin(bits)]
    return ''.join([Base64_table[x] for x in sextets_list])


def from_base_64(string):
    sextets_list = [get_key(x) for x in string]
    bits = ''.join([get_bin(x, 6) for x in sextets_list])
    octests_list = [to_int(x) for x in _to_octets_bin(bits)]
    return ''.join(octest_to_str(x) for x in octests_list)


def _to_sextets_bin(bits, n=6):
    result = [bits[i:i + n] for i in range(0, len(bits), n)]
    if len(result[-1]) < n:
        for x in range(0, (n - len(result[-1]))):
            result[-1] += '0'
    return result


def _to_octets_bin(bits, n=8):
    result = [bits[i:i + n] for i in range(0, len(bits), n)]
    if len(result[-1]) < n:
        result.pop()

    print('to_octets_bin', 'result', result)
    return result