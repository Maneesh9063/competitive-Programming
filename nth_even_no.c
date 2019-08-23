#include <stdio.h>
int find_even(int);
int a[100];
void main()
{
    int k,i;
    scanf("%d",&k);
    for(i=0;a[i-1]!=-1;i++)
        scanf("%d",&a[i]);
    printf("%d",find_even(k));
}
int find_even(int k)
{
    int ans,i,count=0;
    for(i=0;a[i]!=-1;i++){
        if(a[i]%2==0){
            count++;
            ans = a[i];
        }
    }
    if(k==count)
        return ans;
    else
        return -1;

}
