class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        l=len(words)
        for i in range(0,l):
            n=len(words[i])
            for j in range(i+1,l):
                if words[i]==words[j][:n] and words[i]==words[j][-n:]:
                    c+=1
        return c

