a,b,c = map(int,input().split())

def p(a,b):
  if b == 1:
    return a%c
  elif b%2 == 0:
    value = p(a,b/2)
    return value * value % c
  else:
    value = p(a,b//2)
    return value * value * a % c

# 재귀함수 말고 아래에서 %c로 나누면 시간초과 발생
print(p(a,b))