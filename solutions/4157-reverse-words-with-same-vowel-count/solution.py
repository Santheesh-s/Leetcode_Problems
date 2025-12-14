class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        s=s.split()
        cnt=len([i for i in s[0] if i in "aeiou"])
        res+=s[0]
        for j in s[1:]:
            cnt1=len([i for i in j if i in "aeiou"])
            if(cnt1==cnt):
                res+=' '+j[::-1]
            else:
                res+=' '+j
        return res
