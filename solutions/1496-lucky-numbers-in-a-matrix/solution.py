class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ls=[]
        for i in matrix:
            ls.append(min(i))
        for i in range(len(matrix[0])):
            maxi=0
            for j in range(len(matrix)):
                if matrix[j][i]>maxi:
                    maxi=matrix[j][i]
            if maxi in ls:
                return [maxi]
        return []
