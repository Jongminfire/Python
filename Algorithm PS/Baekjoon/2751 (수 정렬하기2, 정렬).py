num = int(input())
arr = []

for i in range(num):
  arr.append(int(input()))

for j in sorted(arr):
  print(j)

# python은 시간초과가 나서 pypy3로 제출했음