class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        cen=0
        for i in range(n):
            cur=0
            ele=set()
            for j in range(i,n):
                cur+=nums[j]
                ele.add(nums[j])
                if cur in ele:
                    cen+=1
        return cen
