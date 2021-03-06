m = int(input())
n = int(input())
lst = []

def check(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True

for i in range(m,n+1):
  if i <= 1:
    continue
  if check(i) == True:
    lst.append(i)

if len(lst) == 0:
  print(-1)
else:
  print(sum(lst))
  print(min(lst))
