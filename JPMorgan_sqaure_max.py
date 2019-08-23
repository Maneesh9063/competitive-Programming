n = int(input("enter the n value "))
a,dp,i,ans =[],[0]*n,0,0
for _ in range(n):
	a.append(list(map(int,(input().split()))))
while(i<n-1):
	count,j = 0,0
	while (j<n):
		if( count+1 != n):
			dp[count]=(a[i][j]+a[i+1][j])
			dp[count+1]=(a[i][j+1]+a[i+1][j+1])
			ans = max(ans,(dp[count]+dp[count+1]))
		j += 1
		count +=1
	dp = [0]*n
	i += 1
print(ans)

# sample input
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# ans is 54