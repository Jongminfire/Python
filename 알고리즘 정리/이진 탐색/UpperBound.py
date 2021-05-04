# 이분탐색을 사용하므로 lst는 정렬된 상태여야 한다.
lst = [1, 5, 4, 10, 6, 27, 17]
lst.sort()


def lowerBound(lst, target):
    start = 0
    end = len(lst)-1

    """
    target이 lst의 모든 요소보다 클 경우
    
    if lst[-1] < target:
        return -1
    """

    while start < end:
        mid = (start + end) // 2

        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end

# lst에서 target보다 크거나 같은 요소의 최소 인덱스 구하기
