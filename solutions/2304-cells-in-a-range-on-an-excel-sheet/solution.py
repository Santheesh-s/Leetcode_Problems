class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n=[i for i in range(int(s[1]),int(s[-1])+1)]
        l=[chr(i) for i in range(ord(s[0]),ord(s[3])+1)]
        ls=[]
        for i in range(len(l)):
            for j in n:
                ls.append(l[i]+str(j))
        return ls
