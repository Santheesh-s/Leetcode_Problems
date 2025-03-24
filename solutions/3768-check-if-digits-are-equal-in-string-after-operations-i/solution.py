class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[int(i) for i in s]
        while len(s1) > 2:
            s1 = [(s1[i] + s1[i + 1]) % 10 for i in range(len(s1) - 1)]
        return s1[0] == s1[1]
