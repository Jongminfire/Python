from collections import deque

n = int(input())
lst = list(map(int,input().split()))
# 그룹 인원을 최소로 하기 위해 오름차순 정렬
lst.sort()

answer = 0

group = []

for i in lst:
  group.append(i)

  # 그룹의 마지막(i)가 group의 길이보다 작거나 같은 경우 group 초기화하고 그룹수 1증가
  if group[-1] <= len(group):
    group = []
    answer += 1

print(answer)

