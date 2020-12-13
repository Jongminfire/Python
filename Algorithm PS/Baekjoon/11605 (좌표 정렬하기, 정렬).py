num = int(input())
arr = []

for i in range(num):
  arr.append(list(map(int,input().split())))

# key 속성을 이용해서 정렬하기  
for j in sorted(arr, key=lambda x : (x[0], x[1])):
  print(j[0],j[1])
