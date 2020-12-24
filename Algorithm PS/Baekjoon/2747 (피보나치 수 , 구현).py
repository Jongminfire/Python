n = int(input())
lst = [0,1,1]

if n <3:
  print(lst[n])
else :
  for i in range(2,n):
    lst.append(lst[i-1]+lst[i])
  print(lst[n])