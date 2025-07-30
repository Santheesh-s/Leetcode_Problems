class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr=sorted(arr)
        ls=[]
        for i in range(len(arr)-1):
            ls.append(abs(arr[i]-arr[i+1]))
        d=min(ls)
        ls=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==d:
                ls.append([arr[i],arr[i+1]])
        return ls
