str = list(map(list, input().split()))

for i in str:
    i.reverse()

A = str[0][0]+str[0][1]+str[0][2]
B = str[1][0]+str[1][1]+str[1][2]

# 위 방법 대신 str[::-1] 로 문자열 뒤집기 하는게 더 좋은 방법 같다.

if int(A) > int(B):
    print(A)
else:
    print(B)
