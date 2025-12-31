class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        if (target > nums[r]) return r + 1;

        while (l <= r) {
            if (target <= nums[l]) return l;
            if (target > nums[r]) return r + 1;
            l++;
            r--;
        }

        return l;
    }
}
