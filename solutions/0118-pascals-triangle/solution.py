class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ls=[[1]]
        for i in range(0,numRows-1):
            s=[1]
            for j in range(len(ls[i])-1):
                s+=[ls[i][j]+ls[i][j+1]]
            s+=[1]
            ls.append(s)
        return ls
