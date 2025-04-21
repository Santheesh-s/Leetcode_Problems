/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* rs) {
    int *arr=(int *)malloc(n*sizeof(int));
    *rs=n;
    if(n%2==0)
        {
            for(int i=1;i<n;i+=2)
            {
                arr[i]=-i;
                arr[i-1]=i;
            }
            return arr;
        }
        for(int i=1;i<n-1;i+=2)
        {
            arr[i]=-i;
            arr[i-1]=i;
        }
        arr[n-1]=0;
        return arr;
}
