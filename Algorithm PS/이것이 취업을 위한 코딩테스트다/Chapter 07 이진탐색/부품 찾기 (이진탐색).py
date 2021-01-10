def binary_search(item,target,start,end):
  while start <= end:
    mid = (start+end)//2

    if item[mid] == target:
      return True
    
    elif item[mid] < target:
      start = mid + 1

    else:
      end = mid - 1
  
  return False
  

n = int(input())
item = list(map(int,input().split()))
m = int(input())
wish = list(map(int,input().split()))

item.sort()

for i in wish:
  if binary_search(item,i,0,n-1) == True:
    print("yes",end = ' ')
  else:
    print("no",end = ' ')