num = int(input())
arr = []
for i in range (num):
  n = int(input())
  arr.append(n)

  # arr.append(int(input()))로 간단하게 줄일 수 있음

arr.sort()

for i in arr:
  print(i)