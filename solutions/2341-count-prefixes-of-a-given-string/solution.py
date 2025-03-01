class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(1,len(s)+1):
            count+=words.count(s[:i])
        return count
