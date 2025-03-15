class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ls=[j for i in grid for j in i ]
        l=len(ls)
        ls1=list(set(ls))
        ls2=(l**2+l)/2-sum(set(ls1))
        ls3=[i for i in ls if ls.count(i)!=1]
        ls3.append(ls2)
        return ls3[1:]
