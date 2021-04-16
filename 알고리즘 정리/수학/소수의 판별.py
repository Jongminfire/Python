import math


def is_prime_number(x):
    # 2부터 x의 제곱근까지 검사
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False

    return True


print(is_prime_number(8))   # False
print(is_prime_number(7))   # True

# 2부터 x의 제곱근 까지의 모든 자연수에 대해서 연산을 수행해야 하므로 시간 복잡도는 O(N^(1/2))
