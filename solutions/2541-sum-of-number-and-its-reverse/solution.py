class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return True
        i=0
        while(i!=num):
            if i+int(str(i)[::-1])==num:
                return True
            i+=1
        return False
