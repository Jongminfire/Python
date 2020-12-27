n,k = map(int,input().split())
lst = []
ans = 0

for i in range (n):
  num = int(input())
  lst.append(num)

# lst = [int(input()) for _ in range(n)] 으로 입력 받는 방법도 있음

lst.sort(reverse = True)

for i in lst:
  if i <= k:
    ans += (k//i)
    k %= i

print(ans)
