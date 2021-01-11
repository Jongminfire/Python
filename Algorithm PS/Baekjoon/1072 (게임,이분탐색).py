def cal(x,y):
  return int((y*100/x))

x,y = map(int,input().split())
pov = cal(x,y)
ans = 0

start = 1
end = 10000000000-x

while start <= end:
  mid = (start+end)//2
  npov = cal(x+mid,y+mid)
  if npov > pov :
    ans = mid
    end = mid - 1

  else:
    start = mid + 1

if ans == 0:
  print(-1)
else:
  print(ans)