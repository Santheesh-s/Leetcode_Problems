class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum1=0
        for i in range(len(arr)):
            for j in range(len(arr)-1,-1,-1):
                if (i+j)%2==0:
                    sum1+=sum(arr[i:j+1])
        return sum1
