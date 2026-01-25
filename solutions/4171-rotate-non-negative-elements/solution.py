class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        neg=[i for i in nums if i>=0]
        if not neg: return nums
        k=k%len(neg)
        neg=neg[k:]+neg[:k]
        k=0
        for i in range(len(nums)):
            if(nums[i]>=0):
                nums[i]=neg[k]
                k+=1
        return nums
