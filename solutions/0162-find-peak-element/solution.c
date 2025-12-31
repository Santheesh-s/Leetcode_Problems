int findPeakElement(int* nums, int numsSize) {
    int m=nums[0],k=0;
        for(int i=0;i<numsSize;i++)
            if(m<nums[i])
            {
                m=nums[i];
                k=i;
            }
        return k;
}
