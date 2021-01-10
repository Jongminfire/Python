n = int(input())
item = [0] * 1000001

for i in input().split():
  item[int(i)] = 1

m = int(input())
wish = list(map(int,input().split()))

for i in wish:
  if item[i] == 1:
    print("yes",end = ' ')
  else:
    print("no", end = ' ')

# 1000001개의 부품번호 리스트를 만들어서 계수정렬을 이용해서 검사하는 방법