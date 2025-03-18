class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr=sorted(arr)
        ls=[bin(i) for i in arr]
        s=sorted(ls,key=lambda x: x.count('1'))
        return [int(i,2) for i in s]
