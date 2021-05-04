import string


# 숫자 + 알파벳 (대문자)
tmp = string.digits+string.ascii_uppercase


# num을 base진법으로 변환
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


print(convert(10, 2))  # 1010
print(convert(10, 3))  # 101
print(convert(15, 16))  # F
print(convert(15, 8))  # 17
