n,m = map(int,input().split())
coin = []
dp = [10001]* (m+1)
for i in range(n):
  coin.append(int(input()))

coin.sort()

for i in coin:
  dp[i] = 1

for i in range(0,m+1):
  for j in coin:
    dp[i] = min(dp[i-j]+1,dp[i])

if dp[m] == 0:
  print(-1)
else:
  print(dp[m])