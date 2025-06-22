class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        arr=[]
        n=1
        m=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                n+=1
            else:
                if i-1-(i-n)>=2:
                    arr.append([i-n,i-1])
                n=1
            m=i
        if m-(m+1-n)>=2:
            arr.append([m+1-n,m])
        return arr
