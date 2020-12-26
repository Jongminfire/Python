n = int(input())
rope = []
ans = 0

for i in range (n):
  rope.append(int(input()))

rope.sort()

for r in range (len(rope)):
  ans = max(ans,rope[r]*(len(rope)-r))

print(ans)

# 모든 로프의 값을 계산해서 최댓값을 찾았음