def rotate_matrix(lst):
    row_length = len(lst)
    column_length = len(lst[0])

    temp = [[0]*row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            temp[c][row_length - 1 - r] = lst[r][c]

    return temp
