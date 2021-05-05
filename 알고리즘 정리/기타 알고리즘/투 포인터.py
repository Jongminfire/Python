"""
n개의 리스트를 입력 받아 부분합이 m인 개수 세기

투 포인터 알고리즘은 시작과 끝값 (start,end)를 조절하면서
원하는 값을 찾거나 개수를 셀 수 있음

다만 리스트 내 원소에 음수 데이터가 포함되어 있는 경우 투 포인터 알고리즘을 사용 할 수 없음
"""


n, m = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += lst[end]
        end += 1

    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1

    interval_sum -= lst[start]

print(count)


"""
n개의 리스트 중 부분합이 m이상인 개수 세기
(https://www.acmicpc.net/problem/1806)
"""

n, s = map(int, input().split())
lst = list(map(int, input().split()))

INF = int(1e9)
start = 0
end = 0
ans = INF
total = 0

while end < len(lst):
    if total < s:
        total += lst[end]
        end += 1

    while total >= s:
        ans = min(ans, end-start)
        total -= lst[start]
        start += 1

print(ans if ans != INF else 0)


"""
이미 정렬된 두 리스트가 주어질 때 두 리스트의 모든 원소를 합쳐서 정렬한 결과를 반환
"""


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0]*(len(a)+len(b))
i, j, k = 0, 0, 0

while i < n and j < m:
    # B가 전부 처리되었거나 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)
