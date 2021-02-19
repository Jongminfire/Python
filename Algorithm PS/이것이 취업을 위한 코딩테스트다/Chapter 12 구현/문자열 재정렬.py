s = list(map(str,input()))
cap = []
num = 0
s.sort()

for i in s:
  # 알파벳인 경우 (i.isalpha()로도 검사 할 수 있음)
  if i < 'A':
    num += int(i)
  else:
    cap.append(i)

print(''.join(cap)+str(num))