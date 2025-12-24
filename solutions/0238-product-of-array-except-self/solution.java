class Solution {
    public int[] productExceptSelf(int[] nums) {
        // int ans[]=new int[nums.length];
        // for(int i=1;i<nums.length;i++)
        //     nums[i]*=nums[i-1];
        int p=1,z=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==0)
                z++;
            else
                p*=nums[i];
        }
        for(int i=0;i<nums.length;i++)
        {
            if(z>1)
                nums[i]=0;
            else if(z==1)
                nums[i]=(nums[i]!=0?0:p);
            else
                nums[i]=p/nums[i];
        }
        return nums;
    }
}
