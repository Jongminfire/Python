n = int(input())
stack = []
ans = 0

for i in range(n):
  num = int(input())
  
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

if len(stack) == 0:
  print(0)
else:
  for i in stack:
    ans += i
  print(ans)