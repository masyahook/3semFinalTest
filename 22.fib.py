def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(8))
'''O(Fib(n))'''


def fibonacci(n):
    dyn_list = [0, 1]
    for i in range(n-1):
        dyn_list.append(dyn_list[-1]+dyn_list[-2])
    return dyn_list[n]
print(fibonacci(8))
'''O(N)'''