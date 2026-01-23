class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        l=0
        for i in s:
            if i=='A':
                a+=1
                l=0
            elif i=='L':
                l+=1
            else:
                l=0
            if l==3:
                return False
        return True if a<2 else False
