import math

# 2부터 n까지의 모든 수에 대하여 소수 판별
n = int(input())
arr = [True for _ in range(n+1)]    # 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 (2부터 n 제곱근까지 수를 검사)
for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        # i를 제외한 i의 모든 배수 False 처리
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n+1):
    if arr[i]:
        print(i)

"""
에라토스테네스의 체 알고리즘 시간 복잡도는 O(N log logN) 이다.
하나의 소수 판별이 아닌 여러개의 소수를 찾아야 하는 문제에서 효과적으로 사용될 수 있다.
하지만 주어진 범위에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요해 넓은 범위가 주어질 경우 사용하기 힘들다는 단점이 있다.
"""
