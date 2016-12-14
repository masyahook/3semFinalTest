def list_reverse(element):
    for i in range(len(element)//2):
        element[i], element[-1-i] = element[-1-i], element[i]
    return element


def list_reverse_simple(element):
    return element[-1::-1]