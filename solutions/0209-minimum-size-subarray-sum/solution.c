int minSubArrayLen(int target, int* nums, int n) {
    int sum=0,m=INT_MAX;
    for(int left=0,right=0;right<n;right++)
    {
        sum+=nums[right];
        while(sum>=target)
        {
            m=fmin(m,right-left+1);
            sum-=nums[left++];
        }
    }
    return m==INT_MAX?0:m;
}
