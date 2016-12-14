def king(width, height):
    dynamic_list = [[0] * height for i in range(width)]
    for i in range(width):
        dynamic_list[i][0] = 1
    for i in range(1, height):
        dynamic_list[0][i] = 1
    for j in range(1, height):
        for i in range(1, width):
            dynamic_list[i][j] = dynamic_list[i-1][j] + dynamic_list[i][j-1] + dynamic_list[i-1][j-1]
    return dynamic_list[-1][-1]

print(king(6, 7))