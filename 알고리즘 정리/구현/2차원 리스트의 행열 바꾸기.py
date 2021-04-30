board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
new_board = list(map(list, zip(*board)))
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]

string_board = ["abcd", "efgh", "ijkl", "mnop"]
new_board = list(map(list, zip(*string_board)))
# [['a', 'e', 'i', 'm'], ['b', 'f', 'j', 'n'], ['c', 'g', 'k', 'o'], ['d', 'h', 'l', 'p']]
new_string = list(map(''.join, new_board))
# ['aeim', 'bfjn', 'cgko', 'dhlp']

# '*' (unpacking)을 사용하면 리스트 내의 요소만 뽑아 낼 수 있다.
