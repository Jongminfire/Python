n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
start = 0
end = lst[n-1]
result = 0

while start <= end:
  mid = (start+end)//2
  length = 0
  
  for i in lst:
    if mid < i:
      length += i - mid

  if length < m:
    end = mid - 1
  
  else:
    result = mid
    start = mid + 1

print(result)

# 시간초과로 pypy3로 제출하였음