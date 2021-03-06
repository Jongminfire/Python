def check(x,y):
  w = 0
  b = 0

  for i in range(x,x+8):
    for j in range(y,y+8):
      if (i+j)%2 == 0:
        if board[j][i] == "W":
          b += 1
        else:
          w += 1
      else:
        if board[j][i] == "W":
          w += 1
        else:
          b += 1
          
  return min(w,b)

n,m = map(int,input().split())
board = []
answer = 2500

for _ in range(n):
  board.append(list(map(str,input())))

for i in range(len(board[0])-7):
  for j in range(len(board)-7):
    answer = min(answer,check(i,j))

print(answer)