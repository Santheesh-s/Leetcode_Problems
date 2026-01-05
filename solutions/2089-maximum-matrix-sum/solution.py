class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        neg=0
        m=1000000
        s=0
        for i in matrix:
            for j in i:
                if j<0:
                    neg+=1
                a=abs(j)
                s+=a
                m=min(m,a)
        if neg%2==0:
            return s
        else:
            return s-m*2
