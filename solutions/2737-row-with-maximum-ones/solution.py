class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ls=[mat[i].count(1) for i in range(len(mat))]
        return [ls.index(max(ls)),max(ls)]
