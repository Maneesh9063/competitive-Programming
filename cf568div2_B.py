test= int(input())

for _ in range(test):
	a=input()
	b=input()
	flag = True
	if(set(a)==set(b)):
		for i in a:
			if a.count(i)>b.count(i):
				flag = False
		if(flag):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")