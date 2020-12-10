num = int(input())
arr = list(map(int, input().split()))
high = 0
sum = 0

for i in arr:
    if i > high:
        high = i

for i in arr:
    i = i/high*100
    sum += i

print(sum/num)
