class Solution {
    public int[] searchRange(int[] nums, int target) {
        int s[]=new int[2];
        s[1]=-1;s[0]=-1;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                s[1]=i;
            }
        }
        for(int j=nums.length-1;j>=0;j--)
        {
            if(nums[j]==target)
            {
                s[0]=j;
            }
        }
        return s;
    }
}
