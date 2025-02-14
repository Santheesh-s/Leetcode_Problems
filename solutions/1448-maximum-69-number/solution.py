class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        ls=list(str(num))
        for i in range(0,len(ls)):
            if ls[i]=='6':
                ls[i]='9'
                break
        print(ls)
        return int("".join(ls))
        
