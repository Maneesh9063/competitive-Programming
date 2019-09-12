target=int(input())
nums=list(map(int,input().split()))
i,l=0,len(nums)
while i<l:
    if ((target-nums[i]) in nums and nums.index(target-nums[i])!=i ) :
        print([i,nums.index(target-nums[i])])
        exit(0)
    i +=1
