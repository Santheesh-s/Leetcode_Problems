class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        ls=[]
        ls1=[]
        length=len(nums)
        n=0
        for i in range(length):
            if nums[i]<pivot:
                ls.append(nums[i])
                n+=1
            elif nums[i]>pivot:
                ls1.append(nums[i])
                n+=1
        return ls+[pivot]*(length-n)+ls1
