class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)- 1;
        if (target > nums[r]): return r + 1;

        while (l <= r):
            if (target <= nums[l]): return l;
            if (target > nums[r]): return r + 1;
            l+=1;
            r-=1;
        return l;
