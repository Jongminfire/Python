n,m = map(int,input().split())
arr = list(map(int,input().split()))
max = 0

arr.sort()

for i in range (0,n-2):
  for j in range (i+1,n-1):
    for k in range (j+1,n):
      if arr[k] > m:
        break
      num = arr[i]+arr[j]+arr[k]
      if num > max and num <= m:
        max=num

        #대신 result = max(result,arr[i]+arr[j]+arr[k]) 방식도 가능하다

print(max)