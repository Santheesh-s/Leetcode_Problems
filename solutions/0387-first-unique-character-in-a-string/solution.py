class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s;
        s+='@';
        i=0;
        while(s[i]!='@'):
            if(s.count(s[i])==1):
                return a.find(s[i]);
            else:
                s=s.replace(s[i],"")
        return -1
