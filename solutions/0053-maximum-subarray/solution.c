int maxSubArray(int* nums, int n) {
    int sum=nums[0],curr=nums[0];
    for(int i=1;i<n;i++)
    {
        if(curr<0)
            curr=0;
        curr+=nums[i];
        if(sum<curr)
            sum=curr;
    }
    return sum;
}

/*  int sum=nums[0];
    for(int i=0;i<n;i++)
        for(int j=i;j<n;j++)
        {
            int sum1=0;
            for(int k=i;k<=j;k++)
                sum1+=*(nums+k);
            if(sum1>sum)
                sum=sum1;
        }
    return sum;*/
