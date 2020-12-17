A = int(input())
B = str(input())
lst = []
for i in range(len(B)):
  lst.append(A*int(B[i]))

for i in reversed(lst):
  print(i)

print(A*int(B))