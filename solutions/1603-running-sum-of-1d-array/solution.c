/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    *returnSize=numsSize;
    int adder=0;
    for(int i=0;i<numsSize;i++)
    {
        adder+=nums[i];
        nums[i]=adder;
    }
    return nums;
}
