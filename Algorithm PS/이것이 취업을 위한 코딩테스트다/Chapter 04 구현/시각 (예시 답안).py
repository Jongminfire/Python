n = int(input())
count = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count += 1

print(count)

# 1초씩 증가시키면서 문자열에 3이 포함되어 있는 개수를 구하는 코드.
# 완전 탐색 방법으로 규칙이나 개수를 세지 않고 시간을 절약 할 수 있다.