def rotate_matrix(lst):
    row_length = len(lst)
    column_length = len(lst[0])

    temp = [[0]*row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            temp[c][row_length - 1 - r] = lst[r][c]

    return temp


# 혹은 아래 방법으로도 가능하다

def rotated(arr):
    list_of_tuples = zip(*arr[::-1])
    return [list(elem) for elem in list_of_tuples]