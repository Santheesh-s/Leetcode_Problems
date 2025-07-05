class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ls=set()
        for i in set(arr):
            if arr.count(i)==i:
                ls.add(i)
        return max(ls) if len(ls) else -1
