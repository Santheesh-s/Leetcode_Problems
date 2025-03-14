class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=[]
        for i in set(s.lower()):
            if i in s and i.upper() in s:
                ls.append(i.upper())
        if len(ls):
            return max(ls)
        else:
            return ""
            
