array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1 , len(array)):
    if array[min_index] > array[j]:
      min_index = j

  array[i] , array[min_index] = array[min_index], array[i]
  # 스왑

"""
선택정렬 : 가장 작은 값을 선택하는 정렬 알고리즘
O(N^2)의 시간이 소요된다.
"""