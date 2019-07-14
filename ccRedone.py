test = int(input())

while(test!=0):
	n = int(input())
	d=(10**9 )+7
	li = [int(x) for x in range(1,n+1)]
	# print(li)
	for i in range(1,n):
		m1=min(li)
		m2=max(li)
		# print(m1,m2)
		# print(li)
		li.remove(m1)
		# print(li)
		li.remove(m2)
		li.append(m1+m2 +(m1*m2))
	print(li[0]%d)
	test -=1
