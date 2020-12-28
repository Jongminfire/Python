from collections import deque

n,m = map(int,input().split())
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range (n):
  graph.append(list(map(int,input())))

def bfs(x,y):
  q = deque()
  q.append((x,y))

  while q:
    x,y = q.popleft()

    for i in range(4):
      dx = x + move[i][0]
      dy = y + move[i][1]

      if dx < 0 or dx >= n or dy < 0 or dy >= m:
        continue
      
      if graph[dx][dy] == 0:
        continue
      
      if graph[dx][dy] == 1:
        graph[dx][dy] = graph[x][y]+1
        q.append((dx,dy))

bfs(0,0)
print(graph[n-1][m-1])
