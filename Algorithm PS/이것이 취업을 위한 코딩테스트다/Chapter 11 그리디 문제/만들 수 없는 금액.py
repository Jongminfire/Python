n = int(input())
lst = list(map(int,input().split()))
lst.sort()

# 최소의 자연수를 뜻하는 target
target = 1

for i in lst:

  # 남아있는 수가 target 보다 작을 경우 종료
  if target < i:
    break
  
  # 남아있는 수가 target 보다 클 경우 target에 더해줌
  else:
    target += i

print(target)

# '최소 자연수' 를 구하는 문제이기 때문에 lst 배열의 수만 생각해주면 됨