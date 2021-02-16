lst = list(map(int,input()))
zero,one = 0,0
group = []

for i in lst:
  group.append(i)

  # 1 그룹과 0 그룹 수 세기
  if group[0] != group[-1]:
    if group[0] == 0:
      zero += 1
    else:
      one += 1
    group = [i]

if group[0] == 0:
  zero += 1
else:
  one += 1

# 1그룹과 0그룹 중 작은 수 출력
print(min(zero,one))
