class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls=""
        tot=0
        for i in range(0,len(s),k):
            n=0
            for j in range(i,i+k):
                n+=(ord(s[j])-97)
            ls+=chr(n%26+97)
        return ls
