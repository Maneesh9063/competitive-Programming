a = list(map(int,(input().split())))
d= a.pop(-1)
a.sort()
left = (d-(a[1]-a[0]))
right = (d-(a[2]-a[1]))
if left <0:
	left =0
if right <0:
	right =0
print(left+right)