string = str(input())
arr = [0]*26
max = 0
index = -1

for i in string:
    num = int(ord(i))

    if num > 96:
        arr[num - 97] += 1
    elif num > 64:
        arr[num - 65] += 1

for i in range(26):
    if arr[i] > max:
        max = arr[i]
        index = i
    elif arr[i] == max:
        index = -1

if index == -1:
    print("?")
else:
    print(chr(index+65))


""" 

코드가 필요 없이 많이 길게 작성되었음.
다른 분들의 답안을 보고 max , index 등에 대한 공부가 필요함

"""
