def cyclic_shift(element):
    last = element[0]
    for i in range(len(element) - 1):
        element[i] = element[i + 1]
    element[-1] = last
    return element


# def cyclic_shift_full(element, step=1, left=True):
#     last = left and (lambda x: element[:step]) or (lambda x: element[-1:-1-step])
#     rng = left and (lambda x: (0, len(element) - 1)) or (lambda x: (len(element) - 1, 0))
#     cyka_blyad = left and (lambda x:)
#     for i in range(rng()[0], rng()[1], step):
#         element[i] = element[i + 1]
#     element[-1] = last
#     return element