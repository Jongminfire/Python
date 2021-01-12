n = int(input())
lst = [0]*10002
dp = [0]*10002

for i in range(n):
  lst[i] = int(input())

dp[0] = lst[0]
dp[1] = lst[0]+lst[1]
dp[2] = max(lst[0]+lst[2],lst[0]+lst[1],lst[1]+lst[2])

for i in range(3,n+1):
  dp[i] = max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i],dp[i-1])
  
  """
  1. 2칸전의 최대값 + 현재 와인
  2. 3칸전의 최대값 + 1칸 전 와인 + 현재 와인
  3. 현재 와인선택 X (반례: 9 9 1 1 9 9 의 경우 중간의 1을 선택 안 해야함)
  """

print(dp[n])