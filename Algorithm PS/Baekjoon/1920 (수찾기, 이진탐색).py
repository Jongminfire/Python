def binary_search(lst,target,start,end):
  while start <= end :
    mid = (start+end)//2

    if lst[mid] == target:
      return True

    elif lst[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1

  return False

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
wish = list(map(int,input().split()))

lst.sort()

for i in wish:
  if binary_search(lst,i,0,n-1) == True:
    print(1)
  else:
    print(0)