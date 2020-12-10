string = str(input())
arr = []
for i in range(97, 123):
    arr.append(string.find(chr(i)))
    # ord: 문자 -> 아스키코드 , chr: 아스키코드 -> 문자

for i in arr:
    print(i, end=' ')
    # end = '문자열' 을 같이 넣으면 강제 개행되지 않는다.
