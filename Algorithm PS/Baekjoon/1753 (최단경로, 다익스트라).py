import heapq
import sys

INF = int(1e9)

v,e = map(int,sys.stdin.readline().split())
s = int(input())
graph = [[] for _ in range(v+1)]
dist = [INF] * (v+1)

for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dist[start] = 0

  while q:
    d,now = heapq.heappop(q)
    
    if dist[now] < d:
      continue
    else:
      for i in graph[now]:
        cost = d + i[1]
        if cost < dist[i[0]]:
          dist[i[0]] = cost
          heapq.heappush(q,(cost,i[0]))
    
dijkstra(s)

for i in range(1,v+1):
  if dist[i] == INF:
    print("INF")
  else:
    print(dist[i])


# 시간 초과로 pypy3로 제출하였음