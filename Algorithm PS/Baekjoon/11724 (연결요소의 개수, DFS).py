n,m = map(int,input().split())
graph= [[0]*n for i in range(n)]
visited = [0 for i in range(n)]
cnt = 0
for i in range(m):
  s,e = map(int,input().split())
  graph[s-1][e-1] = 1
  graph[e-1][s-1] = 1

def dfs(v):
  visited[v] = 1
  for i in range(n):
    if graph[v][i] == 1 and visited[i] == 0:
      dfs(i)

for i in range(n):
  if visited[i] == 0:
    dfs(i)
    cnt += 1

print(cnt)

# 시간초과 나서 PyPy3로 제출함