class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        star=0
        for i in s:
            if (c&1)==0:
                if i=='*':
                    star+=1
            if i=='|':
                    c+=1
        return star
