class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ls=[sorted(str(1 << i)) for i in range(30)]
        return sorted(str(n)) in ls
