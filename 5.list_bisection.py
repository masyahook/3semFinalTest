def upper_bound(element, key):
    left, right = -1, len(element)
    while right - left > 1:
        middle = (left + right)//2
        if element[middle] > key:
            right = middle
        else:
            left = middle
    return right
element, key = sorted([-1, -1, -1, 2, 4, 5, 6, 6]), 2
i = upper_bound(element, key)
if element[i-1] == key:
    print('Найден')