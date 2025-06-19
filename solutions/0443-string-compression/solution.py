class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s=chars[0]
        n=1
        for i in range(1,len(chars)):
            if s[-1]==chars[i]:
                n+=1
            else:
                if n!=1:
                    s=s+str(n)
                s=s+chars[i]
                n=1
        if n!=1:
            s=s+str(n)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)
