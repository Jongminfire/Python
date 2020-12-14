n,m = map(int,input().split())
count = 0

while n != 1:
  if n % m == 0:
    n //= m
    count += 1
  else:
    n -= 1
    count += 1

print(count)

"""
이와 같이 하나씩 n을 빼는 방법으로는 수가 커졌을 때 시간초과 날 수 있으므로
target = (n//m) * m         # n가 가장 가까운 m의 배수
count += (n-target)
n = target

으로 m으로 나눠지는 값을 한번에 빼는 방법도 있다.
"""