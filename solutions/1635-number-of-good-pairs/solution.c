int numIdenticalPairs(int* nums, int numsSize) {
    int n=numsSize,count=0;
    for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
            if(nums[i]==nums[j])
                count+=1;
    return count;
}
