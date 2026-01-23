class Solution {
    public long countBadPairs(int[] nums) {
        for(int i=0;i<nums.length;i++)
            nums[i]-=i;
        long count=0,goodPairs=0;
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++)
        {
            if(nums[i]==nums[i+1])
            {
                count++;
                goodPairs+=count;
            }
            else
                count=0;
        }
        return ((long)(nums.length-1)*nums.length)/2-goodPairs;
    }
}
