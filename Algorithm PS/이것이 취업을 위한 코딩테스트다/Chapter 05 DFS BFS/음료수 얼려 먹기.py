n,m = map(int,input().split())
graph = []
cnt = 0
move = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  graph[x][y] = 1  
  
  for i in range (4):
    dy = y + move[i][0]
    dx = x + move[i][1]
    if dx < 0 or dx >= n or dy <0 or dy >= m :
      continue

    if graph[dx][dy] == 0:
      dfs(dx,dy)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      cnt += 1
      dfs(i,j)

print(cnt)