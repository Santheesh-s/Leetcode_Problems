class Solution {
    public int removeDuplicates(int[] nums) {
        int write=1,n=nums.length;
        for(int i=1;i<n;i++)
            if(nums[i]!=nums[i-1])
                nums[write++]=nums[i];
        return write;
    }
}
