def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_cycle(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd_cycle(43254454556456434600, 43234000))