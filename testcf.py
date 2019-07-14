
rows,cols = (map(int,input().split()))
mat = []
#input each row at a time,with each element separated by a space
for i in range(rows):
   mat.append(input())

d = False  
i=0
while i < rows:
	x=mat[i].find("*")
	if i == rows-1:
		break
	elif x>-1 and (mat[i+1][x]=="*" and mat[i+1][x-1]and mat[i+1][x+1]):
		print("YES")
	else:
		print("NO")
	i +=1 
