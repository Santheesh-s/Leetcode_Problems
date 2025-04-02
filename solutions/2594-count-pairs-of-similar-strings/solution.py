class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """  
        l,c=len(words),0
        for i in range(l):
            n=set(list(words[i]))
            for j in range(i+1,l):
                if n==set(list(words[j])):
                    c+=1
        return c
