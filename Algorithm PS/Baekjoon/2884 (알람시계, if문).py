a, b = map(int,input().split())
if b<45:
	b=15+b
	if a>0:
		a=a-1
	else:
		a=23
else:
	b=b-45
print(a,b,sep=" ")