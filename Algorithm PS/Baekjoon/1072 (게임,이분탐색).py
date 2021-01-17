def cal(x,y):
  return int((y*100/x))         # int((y/x)*100) 으로 하면 오답처리 돼서 수정함

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