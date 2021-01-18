import heapq
import sys

n = int(input())
q = []
for i in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    if len(q) == 0:
      print("0")
    else:
      print(heapq.heappop(q)[1])
  else:
    heapq.heappush(q,(-num,num))
    # heapq는 최소힙을 지원하므로 튜플 형식으로 -num으로 최대힙을 구현