class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            if -int(str(x)[1:][::-1])<-2**31:
                return 0
            else:
                return -int(str(x)[1:][::-1])
        if int(str(x)[::-1])>2**31-1:
            return 0
        else:
            return int(str(x)[::-1])
