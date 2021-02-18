n = list(map(int,input()))

# 0부터 절반-1 까지
a = sum(n[:len(n)//2])

# 절반부터 끝 까지
b = sum(n[len(n)//2:])

if a == b:
  print("LUCKY")
else:
  print("READY")