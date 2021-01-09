from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = []
visited = [[False]*m for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(sx,sy):
  dq = deque()
  dq.append((sx,sy))

  if sy == n-1 and sx == m-1:
    return

  while dq:
    x,y = dq.popleft()
    visited[y][x]=True

    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]

      if mx < 0 or mx >= m or my < 0 or my >= n:
        continue
      
      if graph[my][mx] == 1 and visited[my][mx] == False:
        graph[my][mx] = graph[y][x] + 1
        dq.append((mx,my))
        visited[my][mx] = True  # 여기서 visited를 True로 바꿔야 시간초과와 메모리초과가 나지 않았음

for i in range(n):
  lst = list(map(int,sys.stdin.readline().rstrip()))
  graph.append(lst)

bfs(0,0)
print(graph[n-1][m-1])