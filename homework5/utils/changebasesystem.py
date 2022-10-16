base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


def all_hex(str):
    g = ''
    for i in str:
        grti = hex2bin(i)
        if (len(grti) < 4):
            grti = (4 - len(grti)) * "0" + grti
        g = g + grti
    return g
