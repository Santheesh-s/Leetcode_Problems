class Solution {
    public boolean isGood(int[] nums) {
         Arrays.sort(nums);
        int max=nums.length-1;
        int count=1;
        for(int i=0;i<max;i++)
        {
            if(nums[i]==count)
                count++;
            else
                return false;
        }
        if(count-1==nums[nums.length-1])
            return true;
        return false;
    }
}
