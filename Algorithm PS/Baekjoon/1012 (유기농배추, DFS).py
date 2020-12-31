import sys
sys.setrecursionlimit(100000)
# 재귀 깊이 한도 설정 (런타임에러 제거)

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,graph,visited,m,n):
  visited[y][x] = True

  for i in range(4):
    newX = x+dx[i]
    newY = y+dy[i]

    if newX < 0 or newX >= m or newY < 0 or newY >= n:
      continue
    
    if graph[newY][newX] == 1 and visited[newY][newX] == False:
      dfs(newX,newY,graph,visited,m,n)


for i in range (t):
  m,n,k = map(int,input().split())
  graph = [[0]*m for i in range(n)]
  visited = [[False]*m for i in range(n)]
  cnt = 0

  for j in range (k):
    w,h = map(int,input().split())
    graph[h][w] = 1

  for y in range (n):
    for x in range (m):
      if graph[y][x] == 1 and visited[y][x] == False:
        dfs(x,y,graph,visited,m,n)
        cnt += 1
    
  print(cnt)