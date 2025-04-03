class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ls=[]
        for i in range(len(matrix[0])):
            ls1=[0]*len(matrix)
            for j in range(len(matrix)):
                ls1[j]=matrix[j][i]
            ls.append(ls1)
        return ls
