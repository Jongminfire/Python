test = int(input())

for t in range(test):
  n = int(input())
  lst = set(map(int,input().split()))
  m = int(input())
  wish = list(map(int,input().split()))

  for i in wish:
    if i in lst:
      print(1)
    else:
      print(0)