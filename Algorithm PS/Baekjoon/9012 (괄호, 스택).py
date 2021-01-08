n = int(input())

for i in range(n):
  bracket = str(input())
  stack = []

  for j in bracket:
    if j == '(':
      stack.append(1)
    elif j ==')':
      if len(stack) == 0:
        stack.append(1)         # )의 짝이 맞지 않는 경우 NO 출력을 위해 stack에 append 후 break
        break
      else:
        stack.pop()
  
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")