/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize) {
    *returnSize=numsSize;
    int *nums1=(int *)malloc(4*numsSize);
    for(int i=0;i<numsSize;i++)
        nums1[i]=nums[nums[i]];
    return nums1;
}
