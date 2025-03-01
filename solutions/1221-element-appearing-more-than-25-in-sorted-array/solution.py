class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ls,r,ls1=0,0,list(set(arr))
        for i in ls1:
            if arr.count(i)>ls:
                ls=arr.count(i)
                r=i
        return r
