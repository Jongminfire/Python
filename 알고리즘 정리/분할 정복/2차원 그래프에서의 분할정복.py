n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
white = 0
blue = 0

def divide (x,y,size):
  global blue
  global white
  color = board[x][y]

  for nx in range(x,x+size):
    for ny in range(y,y+size):
      if color != board[nx][ny]:
        divide(x,y,size//2)
        divide(x+size//2,y,size//2)
        divide(x,y+size//2,size//2)
        divide(x+size//2,y+size//2,size//2)

        return
  
  if color == 1:
    blue += 1
  else:
    white += 1

divide(0,0,n)

print(white)
print(blue)

"""
https://www.acmicpc.net/submit/2630/28083282 (백준 2630 색종이만들기 문제)
왼쪽 위, 오른쪽 위,왼쪽 아래,오른쪽 아래의 네 부분으로 나누어서 요소의 개수 세기
"""