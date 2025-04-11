class Solution {
    public int maximumPrimeDifference(int[] nums) {
        int b=0,c=0;
        for(int i=0;i<nums.length;i++)
        {
            if(ss(nums[i]))
            {
                b=i;
                break;
            }
        }
        for(int i=nums.length-1;i>=0;i--)
        {
            if(ss(nums[i]))
            {
                c=i;
                break;
            }
        }
        return Math.abs(c-b);
    }
    public boolean ss(int n)
    {
        if(n<2)
           return false;
        for(int i=2;i<(int)(Math.sqrt(n)+1);i++)
            if(n%i==0)
                return false;
       return true;
    }
}
