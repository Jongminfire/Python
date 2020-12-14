n = int(input())
count = 0

while n % 5 !=0:
  n -= 3
  count += 1

count += n/5

if n >= 0:
  print(int(count))
else:
  print(-1)


# 5로 한번에 나눠지는 값을 찾기 위해 3을 빼주며 카운트 한 뒤, 나머지 값들은 5로 한번에 나누어 주었음.
