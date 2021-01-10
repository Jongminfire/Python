def binary_search(array,target,start,end):
  # 시작점보다 끝점이 클 경우 종료
  if start > end:
    return None

  mid = (start+end) // 2

  # 찾은 경우 mid의 인덱스 반환
  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)

  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array,target,mid+1,end)

n,target = map(int,input().split())
array = list(map(int,input().split()))
array.sort()  # 이진탐색은 정렬된 리스트를 탐색하므로 정렬 시켜준다.

result = binary_search(array,target,0,n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)   # 인덱스이므로 +1 해서 출력