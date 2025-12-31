class Solution {
    public int[] searchRange(int[] nums, int target) {
        int flag1=0,flag2=0;
        int l=0,r=nums.length-1;
        while(l<=r)
        {
            if(flag1==0 )
            {
                if(nums[l]==target)
                    flag1=1;
                else
                    l++;
            }
            if(flag2==0 )
            {
                if(nums[r]==target)
                    flag2=1;
                else
                    r--;
            }
            if(flag1==1 && flag2==1)
                return new int[]{l,r};
        }
        return new int[]{-1,-1};
    }
}
