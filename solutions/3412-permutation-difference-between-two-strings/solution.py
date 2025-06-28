class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)):
            if s[i] in t:
                sum+=abs(i-t.index(s[i]))
        return sum
