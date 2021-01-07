import sys                                          # 입력 시간을 위함
from collections import Counter                     # 최빈값 계산을 위함

n = int(sys.stdin.readline())
lst = []

for i in range(n):
  lst.append(int(sys.stdin.readline()))             # 입력 시간초과 방지를 위함

def mode(lst):
  modes = Counter(lst).most_common()                # Counter(lst)시 dictionary 구조로 반환되는데, most_common() 함수 사용시 리스트 형식으로 반환 됨 (최빈값 순서대로)
  if len(lst) > 1:
    if modes[0][1] == modes[1][1]:
      return modes[1][0]
    else:
      return modes[0][0]
  else:
    return modes[0][0]

lst.sort()

print(round(sum(lst)/n))
print(lst[n//2])
print(mode(lst))                                    # 최빈값을 함수로 정의하지 않으면 오답으로 나와서 함수로 정의했음
print(lst[n-1]-lst[0])