class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        for num in nums:
            curr=num
            while stack and stack[-1]==curr:
                stack.pop()
                curr*=2
            stack.append(curr)
        return stack
