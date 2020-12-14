n = int(input())
p = str(input())
ans = int(p.count('S')+p.count('L')/2)+1

if ans > n:
  print(n)
else:
  print(ans)

# S와 L의 개수를 센 뒤 사람보다 컵홀더가 많을 경우 사람의 수를 출력, 그 이외에는 컵홀더 개수를 출력했음 