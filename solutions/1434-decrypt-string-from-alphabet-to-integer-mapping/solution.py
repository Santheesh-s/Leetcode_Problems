class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ch=[chr(i) for i in range(97,97+26)]
        ls,s,l=[],s[::-1],""
        a,i=len(s),0
        while(i<a):
            if s[i]=='#':
                ls.append(s[i+1]+s[i+2])
                i+=3
            else:
                ls.append(s[i])
                i+=1
        ls=ls[::-1]
        for i in range(len(ls)):
            l+=ch[int(ls[i][::-1])-1]
        return l
