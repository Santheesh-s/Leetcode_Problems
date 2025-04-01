class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in arr2:
            ls=ls+[i]*(arr1.count(i))
        s=[i for i in sorted(arr1) if i not in arr2]
        return ls+s
