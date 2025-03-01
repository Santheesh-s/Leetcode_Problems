class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ls1=[]
        ls=set(arr)
        for i in ls:
            if i==arr.count(i):
                ls1.append(i)
        if len(ls1): return max(ls1)
        else: return -1
