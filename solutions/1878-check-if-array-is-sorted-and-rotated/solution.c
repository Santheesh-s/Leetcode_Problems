bool check(int* nums, int numsSize) 
{
    int start=-1,flag=0,n=numsSize;
    for(int i=0;i<n-1;i++)
    {
        if(flag==0)
            if(nums[i]>nums[i+1])
            {
                start=i;
                flag=1;
            }
        if(start!=i)
            if(nums[i]>nums[i+1])
                return false;
    }
    if(start==-1)
        return true;
    if(nums[0]<nums[n-1])
        return false;
    return true;
}
