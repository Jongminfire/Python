array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0]  # 피벗은 첫 번째 원소
  tail = array[1:]  # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

"""
퀵 정렬: pivot을 기준으로 양 쪽으로 나눈 뒤 합치는 정렬 알고리즘
평균 O(NlogN), 최악일 경우 O(N^2) 시간이 소요된다.
"""