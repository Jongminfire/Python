x,y,w,h = map(int,input().split())

print(min(min(abs(h-y),y),min(abs(x-w),x)))