n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 1
end = max(tree)
answer = 0

while start <= end:
    mid = (start+end)//2
    value = 0

    # 나무를 자른 값 계산
    for i in tree:
        if i >= mid:
            value += i-mid

    # 나무를 자른 값이 목표보다 작을 경우 자르는 길이를 줄인다.
    if value < m :
        end = mid-1
    # 나무를 자른 값이 목표보다 클 경우 길이의 최대값을 구해야 하므로 자르는 길이를 늘인다.
    else:
        start = mid + 1
        answer = mid

print(answer)

"""
파라메트릭 서치는 이진탐색과 비슷한 형식을 가지며
주어진 범위 내에서 원하는 값 또는 원하는 조건에 가장 일치하는 값을 찾아내는 알고리즘이다.
위 문제는 파라메트릭 서치의 기본 문제인 나무자르기 (https://www.acmicpc.net/problem/2805) 문제이다.
주어진 tree를 자른 값이 m 이상이여야 할 때 자를 수 있는 최대 값을 찾는 문제이다
"""