n = int(input())
lst = [0]
dp = [0]

for i in range(n):
  l = list(map(int,input().split()))
  lst.append(l)
  dp.append([0]*len(l))

dp[n] = lst[n]

for i in range(n,0,-1):
  for j in range(0,len(lst[i])-1):
    dp[i-1][j] = max(dp[i][j],dp[i][j+1])+lst[i-1][j]

print(dp[1][0])