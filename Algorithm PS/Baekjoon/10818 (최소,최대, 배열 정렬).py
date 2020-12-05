num = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[0], data[num-1])
