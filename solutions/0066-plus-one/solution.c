/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int n, int* returnSize) {
    *returnSize=n;
    for(int i=n-1;i>=0;i--)
    {
        if(digits[i]<9)
        {
            digits[i]++;
            return digits;
        }
        digits[i]=0;
    }
    *returnSize=n+1;
    int *arr=(int*)calloc(n+1,sizeof(int));
    arr[0]=1;
    return arr;
}
