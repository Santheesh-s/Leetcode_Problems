class Solution {
    public int removeDuplicates(int[] nums) {
        int write=2,n=nums.length;
        for(int i=2;i<n;i++)
            if(nums[i]!=nums[write-2])
                nums[write++]=nums[i];
        return write;
    }
}
