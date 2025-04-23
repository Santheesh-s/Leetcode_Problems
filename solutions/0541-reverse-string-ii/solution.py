class Solution(object):
    def reverseStr(self, st, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(st);
        for i in range(0,len(s),2*k):
            s[i:i+k]=s[i:i+k][::-1]
        return "".join(s)
