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

# 혹은 from bisect import bisect_right 로 upper_bound를 구할 수 있음

from bisect import bisect_right

lst = [1,5,7,10,27,2,16,30]
target = int(input())
lst.sort()

idx = bisect_right(lst,target)

# lst에서 target보다 크거나 같은 요소의 최소 인덱스 구하기
