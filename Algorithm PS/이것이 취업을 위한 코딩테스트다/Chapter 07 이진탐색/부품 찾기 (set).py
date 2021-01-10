n = int(input())
item = set(map(int,input().split()))

m = int(input())
wish = list(map(int,input().split()))

for i in wish:
  if i in item:
    print("yes",end = ' ')
  else:
    print("no",end = ' ')

# 중복된 값을 받지 않는 set 자료형을 이용해서 검색