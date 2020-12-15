n = int(input())
lst = list(map(str,input().split()))
coor = [1,1]

for i in range (len(lst)):
  if lst[i] == 'R' and coor[1] != n:
    coor[1] += 1
  elif lst[i] == 'L' and coor[1] != 1:
    coor[1] -= 1
  elif lst[i] == 'U' and coor[0] != 1:
    coor[0] -= 1
  elif lst[i] == 'D' and coor[0] != n:
    coor[0] += 1

print(coor[0],coor[1])

# 입력 받은 값과 범위 검사를 통해 좌표를 움직였음.