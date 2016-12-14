def pow(a, n):
    if n == 0:
        return 1
    return pow(a, n-1) * a
'''O(N)'''


def fastpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fastpow(a*a, n//2)
    else:
        return fastpow(a, n-1) * a
'''O(log(N))'''