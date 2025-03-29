class Solution(object):
    def sumOfEncryptedInt(self, nums):
        m=0
        for i in nums:
            n=str(i)
            m+=int(max(list(n))*len(n))
        return m
