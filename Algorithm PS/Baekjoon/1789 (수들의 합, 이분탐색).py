n = int(input())
start = 0
end = n
ans = 0

def sum_all(n):
  if n%2 == 0:
    return (int((1+n)*(n/2)))
  else:
    return (int((1+n)*int(n/2)+(n+1)/2))

while start <= end :
  mid = (start+end)//2

  if sum_all(mid) > n:
    end = mid -1
  
  else:
    ans = mid
    start = mid + 1
  
print(ans)
