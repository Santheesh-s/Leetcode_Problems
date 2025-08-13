class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        flag=0
        if '.' in queryIP:
            for i in queryIP:
                if i not in ".1234567890":
                    return "Neither"
            iv4=queryIP.split('.')
            if len(iv4)!=4:
                return 'Neither'
            for i in iv4:
                if i=='' or (i[0]=='0' and len(i)>1)  or int(i)<0 or int(i)>255:
                    return 'Neither'
            return 'IPv4'
        iv6=queryIP.split(':')
        if len(iv6)!=8:
            return "Neither"
        for i in iv6:
            if len(i)>4 or i=='':
                return 'Neither'
            for j in i:
                if j not in "1234567890abcdefABCDEF":
                    return 'Neither'
        return "IPv6"
