class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        for i in range(2,num+1):
            st=map(int,list(str(i)))
            if sum(st)%2==0:
                count+=1
        return count
