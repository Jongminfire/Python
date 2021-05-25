div = 1


def multi(m1, m2):
    ans = []
    for i in range(len(m1)):
        lst = []
        for j in range(len(m2[0])):
            temp = 0
            for k in range(len(m1[0])):
                temp += m1[i][k] * m2[k][j]
            lst.append(temp % div)
        ans.append(lst)

    return ans

# 행렬의 제곱의 요소를 c로 나눈 결과 값 반환
