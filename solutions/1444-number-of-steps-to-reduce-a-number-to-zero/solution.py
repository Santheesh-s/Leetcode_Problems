class Solution(object):
    def numberOfSteps(self, n):
        """
        :type num: int
        :rtype: int
        """
        count=0
        while(n!=0):
            if n%2==0:
                n=n/2
            else:
                n-=1
            count+=1
        return count
