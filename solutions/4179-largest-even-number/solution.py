class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=-1
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2!=0:
                k=i
            else:
                return s[:i+1];
        return ""
            
