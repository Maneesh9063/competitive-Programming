test = int(input())

while test > 0 :
    l = int(input())
    k = int(input())
    a = []
    even = []
    odd = []
    flag = false
    
    for i in range(l) :
        a.append(int(input()))
        if(a[i]%2==0) :
            even.append(int(input()))
        else :
            odd.append(int(input()))
    if(k%2==0) :
        for i in range(max(len(even),len(odd))) :
            if(i<len(even)) :
               # x = int(k -even[i])
                if(even.count(int(k -even[i]))>1):
                    print("True")
                    flag = True
                    break
            if(i<len(odd)) :
                #x = 
                if(odd.count(int(k -odd[i]))>1):
                    print("True")
                    flag = True
                    break
    else :
        for i in range(len(odd)) :
                if(even.count(int(k - odd[i]))>0) :
                        print("True")
                        flag = True
                        break
    test -=1                   
            