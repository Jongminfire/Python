n = int(input())
lst = []
for i in range(n):
  data = input().split()
  lst.append((data[0],int(data[1])))

def sort(data):
  return data[1]

lst.sort(key=sort)
# lst = sorted(lst, key=lambda student: student[1]) 로도 가능하다

for i in lst:
  print(i[0],end = ' ')