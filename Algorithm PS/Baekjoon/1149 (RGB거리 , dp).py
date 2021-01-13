n = int(input())
lst = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1,n+1):
  lst2 = list(map(int,input().split()))
  lst[i] = lst2
  dp[i] = [0,0,0]

dp[1] = lst[1]

for i in range(2,n+1):
  dp[i][0] = min(dp[i-1][1],dp[i-1][2])+lst[i][0]
  dp[i][1] = min(dp[i-1][0],dp[i-1][2])+lst[i][1]
  dp[i][2] = min(dp[i-1][1],dp[i-1][0])+lst[i][2]

print(min(dp[n]))