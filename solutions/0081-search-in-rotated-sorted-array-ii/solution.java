class Solution {
    public boolean search(int[] nums, int target) {
        if(target<=nums[nums.length-1])
            for(int i=nums.length-1;i>=0 && nums[i]>=target;i--)
                if(nums[i]==target)
                    return true;
        for(int i=0;i<nums.length && nums[i]<=target;i++)
            if(nums[i]==target)
                return true;
        return false;
    }
}
