class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        
        j=0
        for i in arr:
            if arr.count(i)==1:
                j+=1
                if j>=k:
                    return i
        return ""
        """
        ls=[i for i in arr if arr.count(i)==1]
        return "" if k>len(ls) else ls[k-1]
