n, count = map(int, input().split())
init = [list(map(int, input().split())) for _ in range(n)]
c = 1


def multi(m1, m2):
    ans = []
    for i in range(len(m1)):
        lst = []
        for j in range(len(m2[0])):
            temp = 0
            for k in range(len(m1[0])):
                temp += m1[i][k] * m2[k][j]
            lst.append(temp % c)
        ans.append(lst)

    return ans


def squared(matrix, p):
    if p == 1:
        return matrix

    div = squared(matrix, p//2)
    squared_div = multi(div, div)

    if p % 2 == 0:
        return squared_div
    else:
        return multi(squared_div, matrix)


for i in squared(init, count):
    print(*i)

# nxn 행렬의 size 제곱의 원소를 c로 나눈 결과
