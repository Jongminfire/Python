def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif arr[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

n , target = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result = binary_search(arr,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


"""
이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용 할 수 있는 알고리즘이다.
탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있으며 O(log N)의 시간복잡도를 가진다.
특히 코딩테스트에서 탐색 범위가 2000만을 넘어가는 큰 범위를 가지는 문제의 경우 이진 탐색으로 접근하는 것이 좋다.
"""