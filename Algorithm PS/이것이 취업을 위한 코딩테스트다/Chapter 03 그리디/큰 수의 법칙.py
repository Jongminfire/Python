n,m,k = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0

lst.sort(reverse=True)

for i in range (1,m+1):
  if i%(k+1) == 0:
    ans += lst[1]
  else:
    ans += lst[0]

print(ans)


"""
이렇게 풀면 값이 많아졌을 때 시간초과가 날 수 있음
따라서 k+1의 수열로 반복된다고 생각 해서

count = m // (k+1) * k 

로 가장 큰 값이 총 몇번 나오는지 계산 한 뒤

ans += count * lst[0]
ans += (m-count) * lst[1]

로 푸는 것이 좋아보임
"""


