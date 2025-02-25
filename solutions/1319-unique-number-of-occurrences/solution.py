class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ls=set(arr)
        ls1=[]
        for i in ls:
            ls1.append(arr.count(i))
        return len(ls1)==len(set(ls1))
