int compare(const void *a, const void *b)
{
    int x = *(const int *)a;
    int y = *(const int *)b;

    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int singleNumber(int* nums, int numsSize) {
    qsort(nums,numsSize,sizeof(int),compare);
    for(int i=0;i<numsSize;i+=3)
    {
        if(i+1>=numsSize)
            return nums[i];
        if(nums[i]==nums[i+1])
            continue;
        else
            return nums[i];
    }
    return 0;
}
