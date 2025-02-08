class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ls=[]
        for i in range(0,n+1):
            ls.append(bin(i).count('1'))
        return ls
        
