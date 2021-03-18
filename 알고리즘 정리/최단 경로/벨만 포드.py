import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0                         # 시작 노드에 대해서 초기화

    for i in range(n):                      # 전체 n번 반복
        for j in range(m):                  # 매 반복마다 모든 간선 확인
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

        # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                
                # n번째 반복에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1 :
                    return True
    
    return False

n,m = map(int,input().split())              # 노드의 개수, 간선의 개수 입력받기
edges = []                                  # 모든 간선에 대한 정보를 담는 리스트 만들기
dist = [INF] * (n+1)                        # 최단 거리 테이블을 모두 무한으로 초기화

# 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())        # a번 노드에서 b번 노드로 가는 비용은 c
    edges.append((a,b,c))

negative_cycle = bf(1)                      # 1번 노드에서 시작

if negative_cycle:                          # 음수 순환이 존재 할 경우 -1 출력
    print("-1")
else:
    for i in range(2,n+1):                  # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
        if dist[i] == INF:                  
            print("-1")                     # 도달할 수 없는 경우 -1 출력
        else:
            print(dist[i])                  # 도달할 수 있는 경우 거리를 출력


"""
벨만포드 알고리즘은 음수 간선이 포함되어 있을 때 최단 경로를 구할 수 있다.
다익스트라와 비교해서 매번 모든 간선을 확인하기 때문에 다익스트라 알고리즘의 최적의 해를 포함하며
시간은 느리지만 음수 간선이 있을 때 거리가 음의 무한인 음수 간선 순환을 확인 할 수 있다는 장점이 있다.
"""
