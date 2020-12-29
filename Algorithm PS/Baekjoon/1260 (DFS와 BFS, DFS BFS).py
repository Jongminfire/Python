from collections import deque

n,m,start = map(int,input().split())
graph = [[0]*n for i in range(n)]
visited = [0 for i in range(n)]
visited2 = [0 for i in range(n)]

for i in range (m):
  s,e = map(int,input().split())
  graph[s-1][e-1] = 1
  graph[e-1][s-1] = 1

def dfs(v):
  visited[v] = 1
  print(v+1, end = ' ')
  for i in range (n):
    if graph[v][i] == 1 and visited[i] == 0:
      dfs(i)

def bfs(v):
  dq = deque()
  dq.append(v)
  print('')

  while dq:
    num = dq.popleft()
    visited2[num] = 1
    print(num+1, end= ' ')
    for i in range(n):
      if graph[num][i] == 1 and visited2[i] == 0:
        dq.append(i)
        visited2[i] = 1

dfs(start-1)
bfs(start-1)