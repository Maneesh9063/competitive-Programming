test=int(input())
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
for __ in range(test):
	d=int(input())
	s=sum_digits3(d)
	print(str(d),end="")
	if s==10:
		print(0)
	else:
		print(str(10-(s%10)))