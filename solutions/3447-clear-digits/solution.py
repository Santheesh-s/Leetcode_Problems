class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=[]
        k=0
        for i in range(len(s)-1,-1,-1):
            if s[i] in "1234567890":
                k+=1
            elif s[i]>='A' and s[i]<='z' and k!=0:
                k-=1
            else :
                ls.append(s[i])
        return "".join(ls[::-1])
