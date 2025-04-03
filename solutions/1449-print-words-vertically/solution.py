class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ls=s.split()
        ls1=[]
        n=len(sorted(ls,key=len)[-1])
        for i in range(n):
            s=""
            for j in range(len(ls)):
                if i>=len(ls[j]):
                    s+=' '
                else:
                    s+=ls[j][i]
            ls1.append(s.rstrip())
        return ls1
