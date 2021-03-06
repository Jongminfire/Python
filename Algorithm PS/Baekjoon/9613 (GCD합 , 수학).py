from math import gcd

n = int(input())
for _ in range(n):
  lst = list(map(int,input().split()))
  g = []

  for i in range(1,len(lst)):
    for j in range(i+1,len(lst)):
        g.append(gcd(lst[i],lst[j]))
  
  print(sum(g))