n,m = map(int,input().split())
d = set()
b = set()
ans = []

for i in range(n):
  d.add(str(input()))

for i in range(m):
  b.add(str(input()))

for i in b:
  if i in d:
    ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
  print(i)