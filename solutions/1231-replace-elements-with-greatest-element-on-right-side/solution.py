class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1,0,-1):
            if arr[i]>arr[i-1]:
                arr[i-1]=arr[i]
        del arr[0]
        arr.append(-1)
        return arr
