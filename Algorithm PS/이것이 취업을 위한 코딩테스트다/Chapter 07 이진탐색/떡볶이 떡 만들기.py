def binary_search(lst,target,start,end):
  while start <= end:
    mid = (start+end)//2
    length = 0

    for i in lst:
      if mid < i:
        length += i - mid

    if length >= target :
      result = mid        # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록함
      start = mid + 1
    
    else:
      end = mid - 1

  return result

n,m = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()

print(binary_search(lst,m,lst[0],lst[n-1]))