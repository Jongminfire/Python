n = int(input())
m = int(input())
graph = [[0]*n for i in range(n)]
visited= [False]*n

for i in range (m):
  s,e = map(int,input().split())
  graph[s-1][e-1] = 1
  graph[e-1][s-1] = 1

def dfs(v):
  visited[v]= True
  
  for i in range(n):
    if graph[v][i] == 1 and visited[i]==False:
      dfs(i)

dfs(0)

ans = 0

for i in visited:
  if i == True:
    ans += 1
  
print(ans-1)