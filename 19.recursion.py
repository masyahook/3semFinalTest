def fact(n):
    if n == 0:
        print('крайний случай')
        return 1
    print('прямой ход, n=', n, sep='')
    fn = fact(n-1) * n
    print('обратный ход, n=', n, sep='')
    return fn
print(fact(22))
'''Стек -- это LIFO (last in -- first out) очередь. При вызове рекурсии в стек записывается адрес возврата
 на инструкцию'''