# 10진수 -> n진수 변환 : bin(num), oct(num), hex(num)

num = 18
print(bin(num)) #2진수. 0b10010
print(oct(num)) #8진수. 0o22
print(hex(num)) #16진수. 0x12

# n진수 -> 10진수 변환 : int(num,현재 진수)

num = '10010'
print(int(num, 2))
num = '22'
print(int(num, 8))
num = '12'
print(int(num, 16))
# 결과 모두 18