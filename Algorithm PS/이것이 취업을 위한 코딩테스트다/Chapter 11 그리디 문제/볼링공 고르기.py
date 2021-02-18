n,m = map(int,input().split())
ball = list(map(int,input().split()))

# 중복을 제외한 종류를 얻기 위해 (문제에서는 m이 10이하 이므로 list로 선언해도 됨)
s = set(ball)

answer = 0

# 중복이 하나도 없는 경우 계산
for i in range(1,n):
  answer += i

# 중복된 만큼 빼주기
for i in s:
  answer -= ball.count(i)-1

print(answer)