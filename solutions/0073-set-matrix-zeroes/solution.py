class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        def row(matrix,r,c):
            while(c<m):
                matrix[r][c]=0
                c+=1
        def col(matrix,r,c):
            while(r<n):
                matrix[r][c]=0
                r+=1
        r=[]
        c=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in set(r):
            row(matrix,i ,0)
        for i in set(c):
            col(matrix,0 ,i)
        
