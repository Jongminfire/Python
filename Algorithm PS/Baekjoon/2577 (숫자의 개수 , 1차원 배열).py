A = int(input())
B = int(input())
C = int(input())
# 세줄에 걸쳐서 입력을 받기 때문에 다음과 같이 세번 입력 받았음

arr = [0]*10
multi = A*B*C

for i in str(multi):
    arr[int(i)] += 1

for i in arr:
    print(i)
