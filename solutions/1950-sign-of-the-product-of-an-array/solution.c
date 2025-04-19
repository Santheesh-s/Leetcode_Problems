int arraySign(int* nums, int numsSize) {
    int n=1;
    for(int i=0;i<numsSize;i++)
    {    
        if(nums[i]>0)
            n*=1;
        else if(nums[i]<0)
            n*=-1;
        else
            return 0;
    }
    return n;
}
