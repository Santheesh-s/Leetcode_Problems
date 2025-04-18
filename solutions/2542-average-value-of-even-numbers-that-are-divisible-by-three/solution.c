int averageValue(int* nums, int numsSize) {
    int sum=0,i=0;
        for(int n=0;n<numsSize;n++)
            if(nums[n]%6==0)
            {
                sum+=nums[n];
                i++;
            }
        if(i==0)
            return 0;
        return sum/i;
}
