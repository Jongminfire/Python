array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):                       # 두번째 데이터부터 검사 시작
  for j in range(i,0,-1):                           # 인덱스 i부터 1까지 감소하며 반복 
    if array[j] > array[j-1]:                       # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]   # 스왑
    else:                                           # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)

"""
삽입정렬 : 삽입 정렬은 특정 데이터를 적절한 위치에 삽입하는 알고리즘
O(N^2)의 시간이 소요된다.
"""