n = int(input())
graph = []
visited = [[False]*n for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def dfs(y,x,cnt):
  visited[y][x] = True
  cnt += 1

  for i in range(4):
    x2 = x+dx[i]
    y2 = y+dy[i]

    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= n:
      continue

    if graph[y2][x2] == 1 and visited[y2][x2] == False :
      cnt = dfs(y2,x2,cnt)
  
  return cnt


for i in range(n):
  lst = list(map(int,input()))
  graph.append(lst)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False:
      ans.append(dfs(i,j,0))

ans.sort()

print(len(ans))
for i in ans:
  print(i)