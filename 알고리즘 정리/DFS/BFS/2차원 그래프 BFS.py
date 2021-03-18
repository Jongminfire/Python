from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(sx,sy,graph,visit):
  dq = deque()
  dq.append((sx,sy))
  
  while dq:
    x,y = dq.popleft()
    visit[x][y] = True

    for i in range(4):
      mx = x+dx[i]
      my = y+dy[i]

      if mx < 0 or mx >= n or my < 0 or my >= m:
        continue
      
      if graph[mx][my] == 0 and visit[mx][my] == False:
        dq.append((mx,my))
  
  return visit

print(bfs(0,0,graph,visit))

"""
세로 n과 가로 m이 주어졌을때
2차원 리스트인 graph와 visit 배열을 통해 상하좌우 방향 BFS를 수행하고 visit 출력
"""