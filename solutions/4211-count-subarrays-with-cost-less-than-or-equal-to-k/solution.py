from sortedcontainers import SortedList
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        count=0;
        left=0
        window=SortedList()

        for right in range(n):
            window.add(nums[right])
            while left <=right and (window[-1]-window[0])*(right-left+1)>k:
                window.remove(nums[left])
                left+=1
            count+=(right-left+1)
        return count
