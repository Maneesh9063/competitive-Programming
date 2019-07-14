def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 
	return x 
def gcd_of_li(l):
	num1 = l[0] 
	num2 = l[1] 
	gcd = find_gcd(num1, num2) 
	for i in range(2, len(l)): 
		gcd = find_gcd(gcd, l[i]) 
	return(gcd) 		

test = int(input())
for __ in range(test):
	n = int(input())
	li = [int(x) for x in input().split(" ")]
	if n==2:
		print(sum(li))
	else:
		m1=max(li)
		li.remove(m1)
		print(gcd_of_li(li)+m1)
		

