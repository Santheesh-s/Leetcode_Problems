class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        
        p=""
        count=0
        for i in range(0,len(s)):
            if s[i]==" ":
                count+=1
            if count==k:
                return p
            else:
                p+=s[i]
        return p
        """
        ls=s.split()
        return " ".join(ls[:k]) 
