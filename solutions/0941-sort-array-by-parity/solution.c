/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* nums, int numsSize, int* returnSize) {
        int* arr = (int*)malloc(sizeof(int) * numsSize);
        int k=0;
        int a=numsSize-1;
        for(int i=0;i<numsSize;i++)
        {
            if(nums[i]%2==0)
                arr[k++]=nums[i];
            else
                arr[a--]=nums[i];
        }
        *returnSize=numsSize;
        return arr;
}
