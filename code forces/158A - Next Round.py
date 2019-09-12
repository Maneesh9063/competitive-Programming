n,k =map(int,(input().split()))
l = list(map(int,input().split()))
if l[k-1] == 0:
    print(0)
    exit()
elif k==n:
    print(k)
    exit()
count = 0
for i in l:
    if i >= l[k-1]:
        # print(i)
        count +=1
print(count)



# print(len(l[:k])+1)#l.count(l[k-1])-1)

# print(len(l)-1-l[::-1].index(l[k])+1)
