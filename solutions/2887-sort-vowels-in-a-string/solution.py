class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        ls=iter(sorted([i for i in s if i in "AEIOUaeiou"]))
        for i in s:
            if i not in "AEIOUaeiou":
                res+=i
            else:
                res+=next(ls)
        return res
