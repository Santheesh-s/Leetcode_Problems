class Solution(object):
    def decodeMessage(self, key, message):
        ls=[]
        for char in key:
            if char not in ls and char!=' ':
                ls.append(char) 
        res=""
        for i in message:
            if i==' ':
                res+=' '
            else:
                res+=chr(ls.index(i)+97)
        return res
