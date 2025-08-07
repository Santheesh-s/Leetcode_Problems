class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start=-1
        flag=0
        for i in range(len(nums)-1):
            if flag==0:
                if nums[i]>nums[i+1]:
                    start=i
                    flag=1
            if start!=i:
                if nums[i]>nums[i+1]:
                    return False
        if start==-1:
            return True
        if nums[0]<nums[len(nums)-1]:
            return False
        return True

