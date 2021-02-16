lst = list(map(int,input()))
lst.sort()
answer = 0

for i in lst:
    # 숫자가 1 혹은 0 이거나 답이 1 혹은 0 이라면 곱하기 보다 더하기가 크므로
    if answer <= 1 or i <= 1:
        answer += i
    else:
        answer *= i

print(answer)