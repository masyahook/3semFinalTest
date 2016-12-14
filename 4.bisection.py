def bisection(a, b, eps, funk):
    func = lambda x: eval(funk)
    left, right = a, b
    try:
        assert (func(left) * func(right) < 0)
    except:
        return 'cyka blyad'
    while (right - left) > eps/2:
        c = (left + right)/2
        if func(a) * func(c) < 0:
            right = c
        elif func(c) == 0:
            return c
        else:
            left = c
    return (left + right) / 2
print(bisection(-300, 0, 0.0000000000001, 'x**2 - 5'))
'''Условия: по теореме Больцано-Коши функция должна быть непрерывна на отрезке, а промежуточные значения разных знаков
асимптотика O(log(2,(n-a)/eps))'''