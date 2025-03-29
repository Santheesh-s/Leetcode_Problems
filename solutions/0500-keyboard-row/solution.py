class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ls=[]
        a="qwertyuiopQWERTYUIOP"
        b="asdfghjklASDFGHJKL"
        c="zxcvbnmZXCVBNM"
        for i in words:
            x,y,z=0,0,0
            for j in i:
                if j in a:
                    x+=1
                elif j in b:
                    y+=1
                elif j in c:
                    z+=1
            if x==len(i) or y==len(i) or z==len(i):
                ls.append(i)
        return ls
