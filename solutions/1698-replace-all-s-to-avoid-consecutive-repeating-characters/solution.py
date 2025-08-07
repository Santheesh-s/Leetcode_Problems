class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n==1 and s[0]=='?':
            return 'a'
        def santheesh(a='7',b='7'):
            for i in range(97,97+26):
                if a!=chr(i) and chr(i)!=b:
                    return chr(i)
        s=list(s)
        r=""
        for i in range(n):
            if s[i]=="?" and i!=0 and i!=n-1:
                a=santheesh(s[i-1],s[i+1])
                r+=a
                s[i]=a
            elif s[i]=='?' and i!=0:
                a=santheesh(s[i-1])
                r+=a
                s[i]=a
            elif s[i]=='?' and i!=n-1:
                a=santheesh(s[i+1])
                r+=a
                s[i]=a
            else:
                r+=s[i]
        return r
