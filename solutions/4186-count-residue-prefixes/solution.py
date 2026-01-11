class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        d=set()
        for i in range(len(s)):
            d.add(s[i])
            pre=i+1
            if len(d)==(pre%3):
                count+=1
        return count
            
