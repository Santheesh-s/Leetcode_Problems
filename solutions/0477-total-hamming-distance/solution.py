class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        n=len(nums)
        for i in range(32):
            bitCount = 0;
            for num in nums:
                bitCount += (num >> i) & 1;
            total += bitCount * (n - bitCount);
        return total;
