str = str(input())
moves = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
coor = [int(str[1]),ord(str[0])-96]     # ord(str[0])-ord('a') 도 가능
count = 0

for m in moves:
  x = coor[0]+m[0]
  y = coor[1]+m[1]

  if x > 0 and x < 9 and y > 0 and y < 9:
    count += 1

print(count)