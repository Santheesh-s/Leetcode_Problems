class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        Map<Integer,Integer>map=new HashMap<>();
        int n=nums.length;
        int sum=0,m=Integer.MAX_VALUE;
        for(int left=0,right=0;right<n;right++)
        {
            sum+=nums[right];
            while(sum>=target)
            {
                m=Math.min(m,right-left+1);
                sum-=nums[left++];
            }
        }
        return m==2147483647?0:m;
    }
}
