INF = int(1e9)              # 무한을 의미하는 값으로 10억을 설정

n , m = map(int,input().split())                # 노드의 개수 및 간선의 개수를 입력받기
graph = [[INF] * (n+1) for _ in range(n+1)]     # 2차원 리스트를 만들고 모든 값을 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())            # A에서 B로 가는 비용은 C라고 설정
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])    # a에서 b로 가는것과 a->k , k->b 로 k를 거쳐 가는 것을 비교

# 수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:                   # 도달할 수 없는 경우 , 무한(INIFINITY) 출력
            print("INFINITY", end = " ")
        else:                                   # 도달할 수 있는 경우 거리 출력
            print(graph[a][b], end = " ")
    print()

"""
플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용하는 알고리즘이다.
노드의 개수가 N개인 경우 플로이드 워셜 알고리즘의 총시간 복잡도는 O(N^3)
"""