maxnum = 0
index = 0
arr = [0]*9
for i in range(9):
    arr[i] = int(input())
    if maxnum < arr[i]:
        maxnum = arr[i]
        index = i+1
print(maxnum)
print(index)
