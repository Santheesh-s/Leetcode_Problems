/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distributeCandies(int candies, int num_people, int* returnSize) {
    void santhu(int arr[],int *n,int p,int *a)
    {
        for(int i=0;i<p;i++)
        {
            if(*a+1<=*n)
            {
                arr[i]+=*a+1;
                *n-=(*a+1);
            }
            else
            {
                arr[i]+=*n;
                *n=0;
                break;
            }
            *a+=1;
        }
    }
    int *arr=(int*) calloc(num_people,sizeof(int));
    *returnSize=num_people;
    int a=0;
    while(candies!=0)
        santhu(arr,&candies,num_people,&a);
    return arr;
}
