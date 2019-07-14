n = (input())
a = [int(x) for x in input().split()]

while sorted(a)!=a:
	if sorted(a[(len(a)//2):])==a[(len(a)//2):]:
		a = a[(len(a)//2):]
	elif sorted(a[:(len(a)//2)])==a[:(len(a)//2)]:
		a = a[:(len(a)//2)]
	else:
		a = a[:(len(a)//2)]
print(len(a))
