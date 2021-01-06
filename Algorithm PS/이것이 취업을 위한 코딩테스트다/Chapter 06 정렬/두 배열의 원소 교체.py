n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()                        # a는 오름차순으로 정렬
b.sort(reverse=True)            # b는 내림차순으로 정렬

for i in range(k):
  if a[i] < b[i]:               # a의 최솟값이 b의 최댓값보다 큰 경우만
    a[i],b[i] = b[i],a[i]       # 스왑
  else:
    break                       # a의 최솟값이 b의 최댓값보다 큰 경우 반복문 중지

print(sum(a))                   # a의 합 출력