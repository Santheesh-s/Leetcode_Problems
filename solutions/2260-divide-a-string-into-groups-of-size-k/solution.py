
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n=len(s)%k
        if n!=0:  n=k-n
        s+=fill*n
        result=[]
        for i in range(0, len(s), k):
            result.append(s[i:i+k])
        return result
