def grasshopper_paths_quantity(n):
    path = [0, 1]
    for i in range(n-1):
        path.append(path[-1] + path[-2])
    return path[-1]


def min_cost(n, price):
    dynamic_list = [price[0], price[1]]
    for i in range(2, n+1):
        dynamic_list.append(price[i] + min(dynamic_list[-1], dynamic_list[-2]))
    return dynamic_list[-1]


def min_cost_path(n, price):
    path = [n]
    while path[-1] != 1:
        current = path[-1]
        if min_cost(current - 1, price) < min_cost(current - 2, price):
            path.append(current - 1)
        else:
            path.append(current - 2)
    return path[::-1]

print(min_cost_path(5, [4, 3, 5, 6, 6, 4, 3]))