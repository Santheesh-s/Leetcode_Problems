class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans=0
        sum=0
        n=0;
        for i in range(len(gain)):
            sum=ans+gain[i]+sum;
            if(n<sum):
                n=sum;
        return n;
