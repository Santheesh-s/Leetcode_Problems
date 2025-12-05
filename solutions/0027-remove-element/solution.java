class Solution {
    public int removeElement(int[] nums, int val) {
        int write=0,n=nums.length;
        for(int i=0;i<n;i++)
        {
            if(nums[i]!=val)
                nums[write++]=nums[i];
        }
        return write;
    }
}
