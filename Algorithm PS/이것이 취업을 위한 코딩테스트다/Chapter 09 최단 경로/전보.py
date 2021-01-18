import heapq
import sys

input=sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
cnt = 0
ans = 0

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dist[start] = 0

  while q:
    d,now = heapq.heappop(q)

    if dist[now] < d:
      continue
    
    for i in graph[now]:
      cost = d + i[1]
      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
        
dijkstra(c)

for i in range(1,n+1):
  if i != c:
    if dist[i] != INF:
      cnt += 1
      ans = max(ans,dist[i])

print(cnt,ans)