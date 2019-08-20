n = int(input("n value "))
k = int(input("k value "))

a = []
for i in range(0,n):
	a.append(i+1)

count = 1
pointer = 0
temp=len(a)
while len(a) != 1:
	count +=1
	pointer +=1
	if pointer >= temp:
		pointer=0
	if count == k:
		print("poped -----> "+str(a.pop(pointer)))
		temp = len(a)
		if pointer >= temp:
			pointer=0
		count = 1

print("The final answer"+str(a[0]))

