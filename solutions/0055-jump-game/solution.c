bool canJump(int* nums, int numsSize) {
    int g=numsSize-1;
    for(int i=numsSize-2;i>=0;i--)
        if(i+nums[i]>=g)
            g=i;
    if(g==0)
        return true;
    return false;
}
