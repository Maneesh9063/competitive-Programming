n=int(input())
# i = 1

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
li=[]
for i in range(1,n):
	if sum_digits3(i)%10==0:
		li.append(i)
# print(li)
j=1

for i in li:
	print(str(i)+"-->"+str(j))
	j +=1