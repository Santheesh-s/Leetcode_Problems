class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isprime(n):
            if n<2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n%i==0:
                    return False
            return True

        ls=[]
        s=len(nums)
        for i in range(0,s):
            if isprime(nums[i]):
                ls.append(i)
        return max(ls)-min(ls)
