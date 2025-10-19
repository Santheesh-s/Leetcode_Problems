class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res=""
        while(columnNumber!=0):
            if columnNumber%26==0:
                res=chr(26+64)+res
                columnNumber-=1
            else:
                res=chr(columnNumber%26+64)+res
            columnNumber//=26
        return res
