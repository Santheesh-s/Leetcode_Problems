class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        // If target is greater than the largest element
        if (target > nums[r]) return r + 1;

        while (l <= r) {
            if (target <= nums[l]) return l;
            if (target > nums[r]) return r + 1;

            l++;
            r--;
        }

        return l;
    }
};

