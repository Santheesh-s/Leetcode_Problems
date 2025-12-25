/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i=0,j=numbersSize-1,sum;
    int *arr=(int *)malloc(sizeof(int)*numbersSize);
    *returnSize=2;
    while(i<j)
    {
        sum=numbers[i]+numbers[j];
        if(sum==target)
        {
            arr[0]=i+1;
            arr[1]=j+1;
            return arr;
        }
        else if(sum>target)
            j--;
        else
            i++;
    }
    return arr;
}
