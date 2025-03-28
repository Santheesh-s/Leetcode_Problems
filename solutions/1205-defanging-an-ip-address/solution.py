class Solution(object):
    def defangIPaddr(self, address):
        
        """
        return "[.]".join(address.split("."))
        
        return address.replace('.','[.]')
        """
        s=""
        for i in address:
            if i=='.':
                s+='[.]'
            else:
                s+=i
        return s
