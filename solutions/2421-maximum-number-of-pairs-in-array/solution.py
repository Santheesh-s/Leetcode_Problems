class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c,r=0,0
        for n in set(nums):
            c+=nums.count(n)//2
            if nums.count(n)%2!=0:
                r+=1
        return [c,r]
