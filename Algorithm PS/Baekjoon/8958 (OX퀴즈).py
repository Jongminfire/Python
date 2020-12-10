num = int(input())
arr = []

for i in range(num):
    a = str(input())
    arr.append(a)

for i in arr:
    score = 0
    sum = 0

    for j in i:
        if j == 'O':
            sum += 1
            score += sum

        elif j == 'X':
            sum = 0

    print(score)
