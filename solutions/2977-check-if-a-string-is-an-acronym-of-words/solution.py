class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(s)!=len(words):
            return False
        for i in range(0,len(s)):
            if words[i][0]!=s[i]:
                return False
        return True
