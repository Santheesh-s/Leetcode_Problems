/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    *returnSize=digitsSize;
    for(int i=digitsSize-1;i>=0;i--)
    {
        if(digits[i]<9)
        {
            digits[i]++;
            return digits;
        }
        digits[i]=0;
    }
    *returnSize+=1;
    int *arr=(int*)calloc(digitsSize+1,sizeof(int));
    arr[0]=1;
    return arr;

}
